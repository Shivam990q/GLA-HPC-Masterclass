# Day 4: Machine Learning Pipeline Foundations
## Comprehensive Lecture & Whiteboard Guide

---

### 1. The Real-World ML Pipeline Architecture
Machine learning in production is not just calling `model.fit()`. It follows an end-to-end data lifecycle:

```
[ Raw CSV Data ]
       |
       v
[ Data Validation & Splitting ] ---> (Train / Test Split - 80/20)
       |
       v
[ ColumnTransformer Pipeline ]
  ├── Numeric Features    -> SimpleImputer(median) -> StandardScaler()
  └── Categorical Features -> SimpleImputer(most_frequent) -> OneHotEncoder()
       |
       v
[ Estimator Selection ] ----> (Logistic Regression / Random Forest)
       |
       v
[ Hyperparameter Optimization ] -> (GridSearchCV / StratifiedKFold)
       |
       v
[ Model Evaluation ] -------> (Confusion Matrix, Precision, Recall, ROC-AUC)
       |
       v
[ Serialization ] ----------> (joblib.dump(pipeline, "model.pkl"))
```

---

### 2. Preventing Data Leakage
**Critical Rule**:
*Never fit your preprocessors (scalers, encoders, imputers) on the test dataset!*
- Fit preprocessors **only** on the training set: `preprocessor.fit_transform(X_train)`.
- Use the fitted parameters to transform the test set: `preprocessor.transform(X_test)`.
- Using `Pipeline` from `sklearn.pipeline` guarantees zero data leakage across cross-validation folds.
