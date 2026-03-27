# Model Artifacts

Trained model files and processed data arrays are not tracked in this repository due to file size. All artifacts are available for download from Google Drive.

**Google Drive — models/:** [Download artifacts](https://drive.google.com/drive/folders/1m4KAoLV85kvqSxyrEXhf7xWcHiqNpf4G?usp=drive_link)

---

## Contents

### Trained Models (.pkl) — Google Drive only

| File | Description |
|---|---|
| `xgb_binary_tuned.pkl` | XGBoost tuned — binary classifier (primary model) |
| `xgb_multiclass_tuned.pkl` | XGBoost tuned — multiclass attack category classifier |
| `rf_binary_tuned.pkl` | Random Forest tuned — binary classifier (fallback model) |
| `rf_multiclass_tuned.pkl` | Random Forest tuned — multiclass classifier |
| `lr_binary.pkl` | Logistic Regression — binary |

### Preprocessing Artifacts (.pkl) — Google Drive only

| File | Description |
|---|---|
| `robust_scaler.pkl` | Fitted RobustScaler from Step 3 |
| `pca_95.pkl` | Fitted PCA (95% variance, 3 components) from Step 3 |
| `y_category_labels.pkl` | Attack category label mapping for multiclass target |

### Best Hyperparameter Configs (.json) — Google Drive only

| File | Description |
|---|---|
| `rf_binary_best_params.json` | Best RF params from RandomizedSearchCV (binary) |
| `rf_multiclass_best_params.json` | Best RF params from RandomizedSearchCV (multiclass) |
| `xgb_binary_best_params.json` | Best XGBoost params (binary) |
| `xgb_multiclass_best_params.json` | Best XGBoost params (multiclass) |

### Processed Data Arrays (.npy) — Google Drive only

| File | Description |
|---|---|
| `X_selected.npy` | Feature matrix — 40 SHAP-selected features, RobustScaled (467,589 × 40) |
| `y_binary.npy` | Binary target labels (0 = Benign, 1 = Attack) |
| `y_multiclass.npy` | Encoded attack category labels |

### Feature & Results Reference (.csv) — tracked in git

| File | Description |
|---|---|
| `selected_features.csv` | Names of the 40 SHAP-selected features in order |
| `model_comparison.csv` | Full model comparison table with all metrics across binary and multiclass tasks |

---

## Reproducibility

To reproduce results without downloading artifacts, run the notebooks in order:

```
notebooks/step2_data_collection.ipynb           → Dataset overview & data dictionary
notebooks/step3_eda_feature_engineering.ipynb   → Preprocessing, EDA, feature engineering
notebooks/step4_model_implementation.ipynb      → Model training, tuning, and evaluation
notebooks/step5_bias_fairness_audit.ipynb       → Explainability, bias audit, and mitigations
```

Each notebook saves its outputs to `./models/` automatically. Step 4 includes a Drive sync cell to persist artifacts across Colab sessions.
