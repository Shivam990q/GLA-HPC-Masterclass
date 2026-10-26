# Day 3: Advanced Web Development with Python (FastAPI & Flask)
## Comprehensive Lecture & Whiteboard Guide

---

### 1. Web Architecture: WSGI vs ASGI
- **WSGI (Web Server Gateway Interface - Flask, Django)**:
  - Synchronous request-response model.
  - Each request occupies an entire worker thread until completion.
  - Stalls under I/O-heavy operations (database queries, network calls).
- **ASGI (Asynchronous Server Gateway Interface - FastAPI, Starlette)**:
  - Built on Python's native `asyncio` event loop.
  - Single thread handles thousands of concurrent requests by yielding control during I/O (`await`).
  - Native support for WebSockets, background tasks, and streaming responses.

---

### 2. JWT (JSON Web Token) Authentication Flow
```
Client (Postman / Browser)               Server (FastAPI)
         |                                       |
         | --- POST /login (username, pass) ---> |
         |                                       | Verify password hash (bcrypt)
         |                                       | Generate JWT: Base64(Header.Payload.Signature)
         | <--- Returns { "access_token": ... } - |
         |                                       |
         | --- GET /protected (Bearer Token) --> |
         |                                       | Verify cryptographic signature using SECRET_KEY
         | <--- Returns 200 OK + Resource ------ |
```

---

### 3. WebSockets vs HTTP Polling
- **HTTP**: Unidirectional client-initiated request/response. High handshake overhead.
- **WebSocket (`ws://`)**: Full-duplex, persistent TCP connection. Both client and server can transmit messages instantaneously with zero header overhead. Ideal for real-time dashboards and chat.
