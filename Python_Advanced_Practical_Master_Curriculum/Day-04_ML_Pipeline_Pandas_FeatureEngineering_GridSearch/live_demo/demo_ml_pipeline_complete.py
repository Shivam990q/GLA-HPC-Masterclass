# demo_ml_pipeline_complete.py
# Full Machine Learning Pipeline: Preprocessing, Feature Engineering, GridSearchCV, and Serialization

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

print("="*60)
print("     STEP 1: SYNTHESIZING ENTERPRISE CHURN DATASET        ")
print("="*60)

np.random.seed(42)
n_samples = 2000

data = pd.DataFrame({
    'age': np.random.randint(18, 70, n_samples),
    'monthly_spend': np.random.uniform(500, 15000, n_samples),
    'tenure_months': np.random.randint(1, 60, n_samples),
    'support_calls': np.random.randint(0, 10, n_samples),
    'contract_type': np.random.choice(['Month-to-Month', 'One-Year', 'Two-Year'], n_samples),
    'payment_method': np.random.choice(['Credit Card', 'UPI', 'Net Banking'], n_samples),
})

# Inject target variable with realistic correlation
churn_prob = (
    (data['support_calls'] > 5).astype(int) * 0.4 +
    (data['contract_type'] == 'Month-to-Month').astype(int) * 0.3 +
    (data['monthly_spend'] > 10000).astype(int) * 0.2
)
data['churn'] = (churn_prob + np.random.normal(0, 0.1, n_samples) > 0.45).astype(int)

# Inject synthetic missing values
data.loc[np.random.choice(n_samples, 50), 'monthly_spend'] = np.nan
data.loc[np.random.choice(n_samples, 30), 'contract_type'] = np.nan

print(f"Synthesized {n_samples} records. Churn rate: {data['churn'].mean():.2%}")

print("\n" + "="*60)
print("     STEP 2: PREPROCESSING & PIPELINE ARCHITECTURE         ")
print("="*60)

X = data.drop(columns=['churn'])
y = data['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

num_features = ['age', 'monthly_spend', 'tenure_months', 'support_calls']
cat_features = ['contract_type', 'payment_method']

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, num_features),
    ('cat', cat_pipeline, cat_features)
])

full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

print("\n" + "="*60)
print("     STEP 3: HYPERPARAMETER TUNING VIA GRIDSEARCHCV       ")
print("="*60)

param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [5, 10, None]
}

cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
grid_search = GridSearchCV(full_pipeline, param_grid, cv=cv, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
print(f"Best Hyperparameters: {grid_search.best_params_}")
print(f"Best Cross-Validation Accuracy: {grid_search.best_score_:.4f}")

print("\n" + "="*60)
print("     STEP 4: MODEL EVALUATION & SERIALIZATION             ")
print("="*60)

y_pred = best_model.predict(X_test)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save pipeline to disk
model_filename = "churn_pipeline_model.joblib"
joblib.dump(best_model, model_filename)
print(f"[+] Successfully serialized trained pipeline to: {model_filename}")
