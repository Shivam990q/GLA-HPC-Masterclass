# Day 3: Web Dev Exam & Top Placement Interview Q&A

### Q1: What makes FastAPI significantly faster than Flask and Django?
- **Answer**:
  1. **ASGI vs WSGI**: FastAPI runs on **Starlette** and **Uvicorn** using Python's native asynchronous event loop (`asyncio`), handling high-concurrency non-blocking I/O effortlessly.
  2. **Pydantic Serialization**: FastAPI uses Pydantic (compiled in Rust via Pydantic v2) for lightning-fast schema validation and JSON serialization.
  3. **Automatic OpenAPI/Swagger Documentation**: Native interactive API docs at `/docs` without third-party plugins.

### Q2: How does JWT Authentication work and why is it stateless?
- **Answer**: A JSON Web Token consists of three base64-encoded segments: `Header.Payload.Signature`.
  - The server signs the token using a secret key (`HMAC-SHA256`).
  - When the client sends the token, the server verifies the cryptographic signature without querying a central session database!
  - It is **stateless** because all authorization metadata (user ID, roles, expiration) lives inside the token itself, enabling effortless horizontal scaling across multiple servers.
