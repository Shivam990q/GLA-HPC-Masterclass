# Day 4: ML Pipeline Exam & Top Placement Interview Q&A

### Q1: What is Data Leakage in Machine Learning and how does Scikit-Learn `Pipeline` eliminate it?
- **Answer**: Data leakage occurs when information from outside the training dataset (such as test dataset statistics) is inadvertently used to train the model. For example, if you compute the global mean for `SimpleImputer` or `StandardScaler` across the entire dataset *before* splitting into train/test, the training step has leaked information about the test distribution.
- **Solution**: A `Pipeline` ensures that preprocessors are fitted strictly on training folds during cross-validation, and merely transform the validation/test folds.

### Q2: What is the difference between `GridSearchCV` and `RandomizedSearchCV`?
- **Answer**:
  - `GridSearchCV` exhaustively tests every combination of hyperparameter values in the search grid. Precise, but computationally expensive ($O(\prod |param_i|)$).
  - `RandomizedSearchCV` samples a fixed number of parameter combinations (`n_iter`) from specified distributions. Statistically finds near-optimal hyperparameters in 10% of the compute time.
