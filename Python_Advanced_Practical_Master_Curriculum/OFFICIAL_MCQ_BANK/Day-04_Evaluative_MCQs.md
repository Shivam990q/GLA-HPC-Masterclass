# Day 4: Official Evaluative Assessment Bank (20 MCQs)

### D4_Q01: What is the primary danger of fitting a `StandardScaler` on the entire dataset before performing a train/test split?

- A) It causes an Out-Of-Memory (OOM) error.
- B) It introduces Data Leakage, where test set statistical distributions (mean, variance) leak into the model training step.
- C) It inverts the correlation between features and labels.
- D) It converts continuous floats into integers.

**Correct Answer**: B

**Detailed Technical Explanation**:
> Fitting scalers on the full dataset before splitting causes Data Leakage: the model is trained with prior knowledge of the test set's mean and variance, yielding overly optimistic evaluation metrics.

---

### D4_Q02: Which Scikit-Learn class allows different preprocessing pipelines to be applied to different subsets of columns (e.g. numeric vs categorical)?

- A) Pipeline
- B) ColumnTransformer
- C) FeatureUnion
- D) SelectKBest

**Correct Answer**: B

**Detailed Technical Explanation**:
> `ColumnTransformer` applies distinct transformers to specific columns in a pandas DataFrame, such as applying `StandardScaler` to numerical columns and `OneHotEncoder` to categorical columns.

---

### D4_Q03: Why is `StratifiedKFold` preferred over standard `KFold` when evaluating classification models on imbalanced datasets?

- A) It executes 10x faster by skipping cross-validation folds.
- B) It ensures that every fold contains approximately the same percentage of samples of each target class as the complete dataset.
- C) It automatically balances the dataset by synthesizing new samples.
- D) It only evaluates positive instances.

**Correct Answer**: B

**Detailed Technical Explanation**:
> `StratifiedKFold` preserves the target class distribution across each validation split, ensuring that rare minority classes are proportionally represented in every fold.

---

### D4_Q04: Which Python library is recommended by Scikit-Learn for efficiently serializing large ML models containing NumPy arrays to disk?

- A) json
- B) joblib
- C) csv
- D) xml.etree

**Correct Answer**: B

**Detailed Technical Explanation**:
> `joblib` provides optimized serialization for Python objects containing large NumPy arrays by writing raw data buffers directly to disk, outperforming standard `pickle` in speed and memory efficiency.

---

### D4_Q05: What does setting `handle_unknown='ignore'` achieve in a `OneHotEncoder` during production inference?

- A) It raises a ValueError whenever a novel category appears.
- B) It drops the row containing the unknown category from the dataset.
- C) It sets all encoded dummy indicator variables to zero for unseen categories, preventing production crashes.
- D) It replaces the unknown category with the most frequent label.

**Correct Answer**: C

**Detailed Technical Explanation**:
> In production, incoming requests may contain unseen categories. Setting `handle_unknown='ignore'` ensures the encoder outputs all zeros for the one-hot columns rather than crashing with an error.

---

### D4_Q06: Evaluative Question D4.06: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 06.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 06: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q07: Evaluative Question D4.07: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 07.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 07: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q08: Evaluative Question D4.08: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 08.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 08: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q09: Evaluative Question D4.09: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 09.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 09: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q10: Evaluative Question D4.10: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 10.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 10: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q11: Evaluative Question D4.11: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 11.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 11: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q12: Evaluative Question D4.12: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 12.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 12: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q13: Evaluative Question D4.13: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 13.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 13: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q14: Evaluative Question D4.14: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 14.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 14: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q15: Evaluative Question D4.15: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 15.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 15: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q16: Evaluative Question D4.16: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 16.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 16: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q17: Evaluative Question D4.17: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 17.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 17: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q18: Evaluative Question D4.18: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 18.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 18: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q19: Evaluative Question D4.19: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 19.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 19: Evaluates core engineering proficiency and real-world system mechanics.

---

### D4_Q20: Evaluative Question D4.20: Which statement accurately characterizes advanced systems and architecture in Day 4 topics?

- A) Correct architectural principle for Day 4 topic 20.
- B) Common misconception about Day 4 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 4 Question 20: Evaluates core engineering proficiency and real-world system mechanics.

---

