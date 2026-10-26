# Day 5: AI Automation Exam & Top Placement Interview Q&A

### Q1: What is the difference between Intent Classification and Named Entity Recognition (NER)?
- **Answer**:
  - **Intent Classification**: A text classification task that determines the overarching goal or purpose of the user's message (e.g. `check_balance` or `book_ticket`).
  - **Named Entity Recognition (NER)**: A sequence tagging task that extracts specific variable entities or tokens from the message (e.g. `amount = 500`, `location = Mathura`, `date = tomorrow`).

### Q2: How do you serve machine learning models in production with low latency?
- **Answer**:
  1. **Model Optimization & Quantization**: Convert models to ONNX or OpenVINO INT8 precision.
  2. **Asynchronous Serving Frameworks**: Use FastAPI / TorchServe / Triton Inference Server rather than heavy WSGI frameworks.
  3. **Batching & Worker Concurrency**: Utilize dynamic batching to group incoming requests and saturate CPU vector units or GPU cores.
