"""
preprocessing.py
----------------
Shared preprocessing utilities for the CICIDS2017 network intrusion detection pipeline.
Functions here are extracted from the notebooks so they can be reused across steps
without copy-pasting.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
import joblib
import os

MODELS_DIR = os.path.join(os.path.dirname(__file__), "..", "models")


# ---------------------------------------------------------------------------
# 1. Label utilities
# ---------------------------------------------------------------------------

ATTACK_CATEGORY_MAP = {
    "BENIGN": "Benign",
    "DoS Hulk": "DoS",
    "DoS GoldenEye": "DoS",
    "DoS slowloris": "DoS",
    "DoS Slowhttptest": "DoS",
    "DDoS": "DDoS",
    "PortScan": "Probe",
    "FTP-Patator": "Brute Force",
    "SSH-Patator": "Brute Force",
    "Bot": "Botnet",
    "Infiltration": "Infiltration",
    "Web Attack \x96 Brute Force": "Web Attack",
    "Web Attack \x96 XSS": "Web Attack",
    "Web Attack \x96 Sql Injection": "Web Attack",
    "Heartbleed": "Other",
}


def map_attack_categories(series: pd.Series) -> pd.Series:
    """Map raw CICIDS2017 label strings to consolidated attack category names."""
    return series.str.strip().map(ATTACK_CATEGORY_MAP).fillna("Unknown")


def make_binary_label(series: pd.Series) -> pd.Series:
    """Return 0 for Benign, 1 for all attack categories."""
    return (series.str.strip() != "BENIGN").astype(int)


# ---------------------------------------------------------------------------
# 2. Data quality
# ---------------------------------------------------------------------------

ZERO_VARIANCE_COLS = [
    "Bwd PSH Flags",
    "Fwd URG Flags",
    "Bwd URG Flags",
    "CWE Flag Count",
    "Fwd Avg Bytes/Bulk",
    "Fwd Avg Packets/Bulk",
    "Fwd Avg Bulk Rate",
    "Bwd Avg Bytes/Bulk",
    "Bwd Avg Packets/Bulk",
    "Bwd Avg Bulk Rate",
]

NEAR_ZERO_VARIANCE_COLS = [
    "Fwd PSH Flags",
    "ECE Flag Count",
    "URG Flag Count",
    "Down/Up Ratio",
]

INFINITE_VALUE_COLS = ["Flow Bytes/s", "Flow Packets/s"]


def drop_low_variance_features(df: pd.DataFrame) -> pd.DataFrame:
    """Drop known zero-variance and near-zero-variance columns from CICIDS2017."""
    cols_to_drop = [
        c for c in ZERO_VARIANCE_COLS + NEAR_ZERO_VARIANCE_COLS if c in df.columns
    ]
    return df.drop(columns=cols_to_drop)


def cap_infinite_values(df: pd.DataFrame, quantile: float = 0.999) -> pd.DataFrame:
    """
    Replace infinite values in rate columns with the given quantile of finite values.
    Modifies in place and returns the dataframe.
    """
    df = df.copy()
    for col in INFINITE_VALUE_COLS:
        if col not in df.columns:
            continue
        finite_vals = df.loc[np.isfinite(df[col]), col]
        cap = finite_vals.quantile(quantile)
        df[col] = df[col].replace([np.inf, -np.inf], np.nan)
        df[col] = df[col].clip(upper=cap).fillna(cap)
    return df


def remove_nan_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows containing NaN values (safe given NaN << 0.05% of dataset)."""
    return df.dropna()


# ---------------------------------------------------------------------------
# 3. Transformations
# ---------------------------------------------------------------------------

def log1p_skewed_features(df: pd.DataFrame, skew_threshold: float = 5.0) -> pd.DataFrame:
    """
    Apply log1p transformation to numeric columns with absolute skewness above
    skew_threshold, provided their minimum value is non-negative.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    skewness = df[numeric_cols].skew()
    cols_to_transform = skewness[abs(skewness) > skew_threshold].index
    for col in cols_to_transform:
        if df[col].min() >= 0:
            df[col] = np.log1p(df[col])
    return df


def fit_robust_scaler(df: pd.DataFrame, feature_cols: list, save: bool = True) -> RobustScaler:
    """Fit a RobustScaler on feature_cols and optionally save to models/."""
    scaler = RobustScaler()
    scaler.fit(df[feature_cols])
    if save:
        path = os.path.join(MODELS_DIR, "robust_scaler.pkl")
        joblib.dump(scaler, path)
    return scaler


def apply_scaler(df: pd.DataFrame, feature_cols: list, scaler: RobustScaler) -> pd.DataFrame:
    """Apply a fitted RobustScaler and return updated dataframe."""
    df = df.copy()
    df[feature_cols] = scaler.transform(df[feature_cols])
    return df


# ---------------------------------------------------------------------------
# 4. Feature engineering
# ---------------------------------------------------------------------------

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add six domain-derived features to the dataframe.

    Features added:
        byte_asymmetry       — directional byte imbalance ratio
        packet_asymmetry     — directional packet count imbalance ratio
        flag_intensity       — (SYN + RST + FIN) / total_packets
        fwd_payload_ratio    — forward payload bytes / forward header bytes
        duration_bin         — ordinal bin of Flow Duration
        is_tcp / is_udp      — binary protocol indicators
    """
    df = df.copy()
    eps = 1e-9

    fwd_b = df.get("Total Length of Fwd Packets", pd.Series(0, index=df.index))
    bwd_b = df.get("Total Length of Bwd Packets", pd.Series(0, index=df.index))
    fwd_p = df.get("Total Fwd Packets", pd.Series(0, index=df.index))
    bwd_p = df.get("Total Backward Packets", pd.Series(0, index=df.index))
    syn   = df.get("SYN Flag Count", pd.Series(0, index=df.index))
    rst   = df.get("RST Flag Count", pd.Series(0, index=df.index))
    fin   = df.get("FIN Flag Count", pd.Series(0, index=df.index))
    total_p = fwd_p + bwd_p
    fwd_header = df.get("Fwd Header Length", pd.Series(1, index=df.index))

    df["byte_asymmetry"] = (fwd_b - bwd_b) / (fwd_b + bwd_b + eps)
    df["packet_asymmetry"] = (fwd_p - bwd_p) / (fwd_p + bwd_p + eps)
    df["flag_intensity"] = (syn + rst + fin) / (total_p + eps)
    df["fwd_payload_ratio"] = fwd_b / (fwd_header + eps)

    duration = df.get("Flow Duration", pd.Series(0, index=df.index))
    df["duration_bin"] = pd.cut(
        duration,
        bins=[-1, 0, 1_000, 100_000, 1_000_000, float("inf")],
        labels=[0, 1, 2, 3, 4],
    ).astype(float)

    protocol = df.get("Protocol", pd.Series(0, index=df.index))
    df["is_tcp"] = (protocol == 6).astype(int)
    df["is_udp"] = (protocol == 17).astype(int)

    return df


# ---------------------------------------------------------------------------
# 5. Dimensionality reduction
# ---------------------------------------------------------------------------

def fit_pca(X: np.ndarray, variance_threshold: float = 0.95, save: bool = True) -> PCA:
    """Fit PCA retaining variance_threshold of explained variance."""
    pca = PCA(n_components=variance_threshold, random_state=42)
    pca.fit(X)
    if save:
        path = os.path.join(MODELS_DIR, "pca_95.pkl")
        joblib.dump(pca, path)
    return pca


def load_artifact(filename: str):
    """Load a saved model artifact from the models/ directory."""
    path = os.path.join(MODELS_DIR, filename)
    return joblib.load(path)
