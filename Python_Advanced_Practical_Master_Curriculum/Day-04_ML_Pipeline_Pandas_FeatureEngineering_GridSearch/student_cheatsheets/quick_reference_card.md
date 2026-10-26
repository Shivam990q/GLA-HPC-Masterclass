# Day 4 Cheatsheet: Scikit-Learn Pipeline Quick Reference

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

preprocessor = ColumnTransformer([
    ('num', Pipeline([('imputer', SimpleImputer()), ('scaler', StandardScaler())]), num_cols),
    ('cat', OneHotEncoder(), cat_cols)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```
