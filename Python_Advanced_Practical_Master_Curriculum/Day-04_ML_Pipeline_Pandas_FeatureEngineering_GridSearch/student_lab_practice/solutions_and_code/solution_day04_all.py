# solution_day04_all.py
# Working solutions for Day 4 ML Pipeline practice problems

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Synthesize Housing Data
np.random.seed(42)
n = 1000
df = pd.DataFrame({
    'area': np.random.uniform(500, 3500, n),
    'bedrooms': np.random.randint(1, 5, n),
    'age': np.random.randint(0, 30, n),
    'locality': np.random.choice(['Mathura Cantt', 'Vrindavan', 'NH-19 Highway'], n),
    'property_type': np.random.choice(['Apartment', 'Villa', 'Independent'], n)
})
df['price'] = (df['area'] * 4500 + df['bedrooms'] * 300000 - df['age'] * 50000 + np.random.normal(0, 100000, n))

X = df.drop(columns=['price'])
y = df['price']

num_cols = ['area', 'bedrooms', 'age']
cat_cols = ['locality', 'property_type']

preprocessor = ColumnTransformer(transformers=[
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), num_cols),
    ('cat', Pipeline([('imp', SimpleImputer(strategy='most_frequent')), ('ohe', OneHotEncoder(handle_unknown='ignore'))]), cat_cols)
])

pipe = Pipeline([
    ('prep', preprocessor),
    ('rf', RandomForestRegressor(n_estimators=30, random_state=42))
])

scores = cross_val_score(pipe, X, y, cv=5, scoring='r2')
print(f"5-Fold Cross Validation R^2: {scores.mean():.4f} +/- {scores.std():.4f}")

pipe.fit(X, y)
joblib.dump(pipe, "housing_pipeline.joblib")
print("[+] Model saved successfully as housing_pipeline.joblib")
