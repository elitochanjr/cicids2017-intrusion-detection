# Model Artifacts

Trained model files and processed data arrays are not tracked in this repository due to file size. All artifacts are available for download from Google Drive.

**Google Drive — models/:** [Download artifacts](https://drive.google.com/drive/folders/1m4KAoLV85kvqSxyrEXhf7xWcHiqNpf4G?usp=drive_link)

---

## Contents

### Trained Models (.pkl)

| File | Description |
|---|---|
| `xgb_binary_tuned.pkl` | XGBoost tuned — binary classifier (primary model) |
| `xgb_multiclass_tuned.pkl` | XGBoost tuned — multiclass attack category classifier |
| `rf_binary_tuned.pkl` | Random Forest tuned — binary classifier (fallback model) |
| `rf_multiclass_tuned.pkl` | Random Forest tuned — multiclass classifier |
| `rf_binary_baseline.pkl` | Random Forest baseline — binary |
| `xgb_binary_baseline.pkl` | XGBoost baseline — binary |
| `lr_binary.pkl` | Logistic Regression — binary |
| `lr_multiclass.pkl` | Logistic Regression — multiclass |
| `label_encoder_multiclass.pkl` | LabelEncoder for attack category labels |

### Preprocessing Artifacts (.pkl)

| File | Description |
|---|---|
| `robust_scaler.pkl` | Fitted RobustScaler from Step 3 |
| `pca_95.pkl` | Fitted PCA (95% variance, 3 components) from Step 3 |

### Best Hyperparameter Configs (.json)

| File | Description |
|---|---|
| `rf_binary_best_params.json` | Best RF params from RandomizedSearchCV (binary) |
| `rf_multiclass_best_params.json` | Best RF params from RandomizedSearchCV (multiclass) |
| `xgb_binary_best_params.json` | Best XGBoost params (binary) |
| `xgb_multiclass_best_params.json` | Best XGBoost params (multiclass) |

### Processed Data Arrays (.npy)

| File | Description |
|---|---|
| `X_selected.npy` | Feature matrix — 40 SHAP-selected features, RobustScaled (467,589 × 40) |
| `y_binary.npy` | Binary target labels (0 = Benign, 1 = Attack) |
| `y_multiclass.npy` | Encoded attack category labels |

### Feature Reference (.csv)

| File | Description |
|---|---|
| `selected_features.csv` | Names of the 40 SHAP-selected features in order |
| `model_comparison.csv` | Full model comparison table with all metrics |

---

## Reproducibility

To reproduce results without downloading artifacts, run the notebooks in order:

```
notebooks/step2_data_collection.ipynb
notebooks/step3_eda_feature_engineering.ipynb
notebooks/step4_model_implementation.ipynb
notebooks/step5_bias_fairness_audit.ipynb
```

Each notebook saves its outputs to `./models/` automatically.
