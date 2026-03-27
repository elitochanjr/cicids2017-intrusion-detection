# Network Intrusion Detection with Machine Learning

**PGD AIML Capstone Project** | Cybersecurity Domain
*Detecting anomalies in network traffic using the CICIDS2017 dataset*

---

## Project Overview

Organizations face growing volumes of network intrusions that evade rule-based security systems. This project builds an end-to-end ML pipeline that classifies network flows as benign or malicious, and where labels permit, identifies the specific attack category (DoS, DDoS, Probe, Botnet, etc.).

The pipeline covers the full ML lifecycle: problem framing, data preprocessing, exploratory analysis, feature engineering, model training and evaluation, explainability, and bias auditing.

**Dataset:** [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) — Canadian Institute for Cybersecurity, University of New Brunswick
**Kaggle mirror:** [chethuhn/network-intrusion-dataset](https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset)

---

## Repository Structure

```
├── notebooks/              # Jupyter notebooks (one per step)
│   ├── step2_data_collection.ipynb
│   ├── step3_eda_feature_engineering.ipynb
│   ├── step4_model_implementation.ipynb
│   └── step5_bias_fairness_audit.ipynb
├── src/                    # Reusable Python modules
│   ├── __init__.py
│   └── preprocessing.py    # Shared preprocessing utilities
├── data/                   # Data directory (files not tracked — see below)
│   └── README.md
├── models/                 # Saved model artifacts (not tracked in git)
│   └── .gitkeep
├── reports/                # Written analysis and final report
│   └── capstone_report.md
├── requirements.txt
└── .gitignore
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/elitochanjr/cicids2017-intrusion-detection.git
cd cicids2017-intrusion-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the dataset

The CICIDS2017 dataset is not tracked in this repository due to file size (~500MB). Download it from Kaggle:

```bash
# Option A: Kaggle CLI (requires kaggle.json credentials)
kaggle datasets download -d chethuhn/network-intrusion-dataset
unzip network-intrusion-dataset.zip -d data/raw/

# Option B: Manual download
# Visit https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset
# Download and extract CSV files into data/raw/
```

### 4. Run the notebooks in order

```
notebooks/step2_data_collection.ipynb       → Dataset overview & data dictionary
notebooks/step3_eda_feature_engineering.ipynb → Preprocessing, EDA, features
```

---

## Pipeline Summary

### Step 1: Problem Framing
Binary classification (Benign vs. Attack) with multi-class extension across 14 attack subtypes. Primary metric: macro F1-Score. Target: Recall ≥ 0.95, FPR ≤ 0.05, AUC-ROC ≥ 0.98.

### Step 2: Data Collection
CICIDS2017: ~500,000 flow records stratified-sampled to 467,589 after deduplication, 78 numeric features from CICFlowMeter. Severe class imbalance (80.3% benign). Three data quality issues addressed: NaN rows, infinite rate values, zero-variance columns.

### Step 3: Preprocessing & Feature Engineering
- 467,589 rows after deduplication; 66 features after zero-variance drop; 29 features log-transformed
- Infinite value capping at 99.9th percentile; RobustScaler for outlier-resistant scaling
- 5 domain-derived features: byte asymmetry, packet asymmetry, flag intensity, payload-to-header ratio, duration bin
- 3-stage feature selection: variance threshold → correlation filter → SHAP top-40 (71 → 51 → 40 features)
- PCA: 95% variance retained in 3 components; t-SNE visualization confirms class separation

### Step 4: Model Implementation *(in progress)*
Multiple supervised models (Logistic Regression, Random Forest, XGBoost) with hyperparameter tuning via RandomizedSearchCV, cross-validation, and saved artifacts. SVM deprioritized due to scaling constraints at 400K+ rows.

### Step 5: Bias & Fairness Audit *(in progress)*
SHAP/LIME/PDP explanations, imbalance and overfitting analysis, fairness evaluation across traffic subgroups.

---

## Model Artifacts

Trained model files (`.pkl`) and processed data arrays (`.npy`) are not tracked in this repository due to file size. Download them from Google Drive:

**[Google Drive — models/](https://drive.google.com/drive/folders/1m4KAoLV85kvqSxyrEXhf7xWcHiqNpf4G?usp=drive_link)**

See `models/README.md` for a full description of every file.

---

## Key Results

| Metric | Target | Achieved |
|---|---|---|
| AUC-ROC | ≥ 0.98 | TBD (Step 4) |
| Macro F1 | — | TBD (Step 4) |
| Attack Recall | ≥ 0.95 | TBD (Step 4) |
| FPR | ≤ 0.05 | TBD (Step 4) |

---

## Tech Stack

- Python 3.10+
- pandas, numpy, scikit-learn
- shap, matplotlib, seaborn
- xgboost
- joblib (model persistence)

---

## License

This project is for educational purposes (PGD AIML Capstone). The CICIDS2017 dataset is provided by the Canadian Institute for Cybersecurity under its own terms of use.
