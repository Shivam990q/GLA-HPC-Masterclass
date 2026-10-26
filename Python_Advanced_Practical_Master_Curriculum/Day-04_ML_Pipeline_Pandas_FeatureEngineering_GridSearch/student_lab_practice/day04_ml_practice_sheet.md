# Day 4: ML Pipeline Practice Sheet (GLA B.Tech CSE)

## Problem 1: End-to-End Pipeline on Synthetic Housing Data
- Build a full Scikit-Learn `Pipeline` for housing price regression:
  - Numeric features (`area`, `bedrooms`, `age`) -> Impute median + StandardScaler.
  - Categorical features (`locality`, `property_type`) -> Impute most frequent + OneHotEncoder.
  - Model: `RandomForestRegressor`.

## Problem 2: K-Fold Cross-Validation & Metric Inspection
- Perform 5-fold cross-validation using `cross_val_score(scoring='r2')`.
- Print the mean $R^2$ score and standard deviation.

## Problem 3: Hyperparameter Optimization & Model Export
- Use `GridSearchCV` to optimize `n_estimators` ([20, 50]) and `max_depth` ([4, 8]).
- Save the best pipeline using `joblib.dump()` and write a test script that loads the file and makes a prediction.
