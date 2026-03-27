# Submission Links — CICIDS2017 Network Intrusion Detection

**Elito Chan Jr.** | PGD Artificial Intelligence & Machine Learning | Cybersecurity Capstone

---

## GitHub Repository

[github.com/elitochanjr/cicids2017-intrusion-detection](https://github.com/elitochanjr/cicids2017-intrusion-detection)

---

## Notebooks

| Step | Notebook | Link |
|---|---|---|
| Step 2 | Data Collection & Understanding | [step2_data_collection.ipynb](https://github.com/elitochanjr/cicids2017-intrusion-detection/blob/main/notebooks/step2_data_collection.ipynb) |
| Step 3 | Preprocessing, EDA & Feature Engineering | [step3_eda_feature_engineering.ipynb](https://github.com/elitochanjr/cicids2017-intrusion-detection/blob/main/notebooks/step3_eda_feature_engineering.ipynb) |
| Step 4 | Model Implementation & Comparison | [step4_model_implementation.ipynb](https://github.com/elitochanjr/cicids2017-intrusion-detection/blob/main/notebooks/step4_model_implementation.ipynb) |
| Step 5 | Bias, Fairness & Explainability Audit | [step5_bias_fairness_audit.ipynb](https://github.com/elitochanjr/cicids2017-intrusion-detection/blob/main/notebooks/step5_bias_fairness_audit.ipynb) |

---

## Reports & Presentations

| File | Link |
|---|---|
| Capstone Report (PDF) | [capstone_report.pdf](https://github.com/elitochanjr/cicids2017-intrusion-detection/blob/main/reports/capstone_report.pdf) |
| Capstone Report (Word) | [capstone_report.docx](https://github.com/elitochanjr/cicids2017-intrusion-detection/blob/main/reports/capstone_report.docx) |
| Technical Presentation | [technical_presentation.pptx](https://github.com/elitochanjr/cicids2017-intrusion-detection/blob/main/reports/technical_presentation.pptx) |
| Business Presentation | [business_presentation.pptx](https://github.com/elitochanjr/cicids2017-intrusion-detection/blob/main/reports/business_presentation.pptx) |

---

## Model Artifacts

Trained models and data arrays are hosted on Google Drive due to file size.

[Google Drive — models/](https://drive.google.com/drive/folders/1m4KAoLV85kvqSxyrEXhf7xWcHiqNpf4G?usp=drive_link)

| File | Description |
|---|---|
| `xgb_binary_tuned.pkl` | XGBoost — binary classifier (primary model) |
| `xgb_multiclass_tuned.pkl` | XGBoost — multiclass attack category classifier |
| `rf_binary_tuned.pkl` | Random Forest — binary classifier (fallback) |
| `rf_multiclass_tuned.pkl` | Random Forest — multiclass classifier |
| `lr_binary.pkl` | Logistic Regression — binary |
| `robust_scaler.pkl` | Fitted RobustScaler |
| `pca_95.pkl` | Fitted PCA (95% variance, 3 components) |
| `X_selected.npy` | Feature matrix (467,589 × 40) |
| `y_binary.npy` | Binary target labels |
| `y_multiclass.npy` | Multiclass target labels |

---

## Key Results

| Metric | Target | Achieved |
|---|---|---|
| AUC-ROC | ≥ 0.98 | 1.0000 (XGBoost Tuned, binary) |
| Attack Recall | ≥ 0.95 | 0.9994 (XGBoost Tuned, binary) |
| Macro F1 (binary) | — | 0.9983 |
| Macro F1 (multiclass) | — | 0.9667 |
| CV Stability (XGBoost) | — | 0.9990 ± 0.0001 (5-fold) |
