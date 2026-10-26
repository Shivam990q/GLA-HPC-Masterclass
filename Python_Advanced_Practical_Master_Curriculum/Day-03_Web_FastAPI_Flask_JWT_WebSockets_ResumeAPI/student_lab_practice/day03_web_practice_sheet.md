# Day 3: Advanced Web Development Practice Sheet (GLA B.Tech CSE)

## Problem 1: FastAPI User CRUD Service
- Implement REST endpoints:
  - `POST /users` (Create user with name, email, role).
  - `GET /users` (List all users with pagination `skip` and `limit`).
  - `GET /users/{user_id}` (Get user by ID, return 404 if not found).
  - `DELETE /users/{user_id}` (Delete user).

## Problem 2: JWT Authentication in Flask / FastAPI
- Create `/auth/login` accepting username and password.
- Validate credentials and return an encoded JWT bearer token with 15-minute expiration.
- Protect `/auth/profile` requiring `Authorization: Bearer <token>`.

## Problem 3: Real-Time WebSocket Echo Server
- Create a WebSocket endpoint `/ws` that broadcasts incoming messages to all connected clients.
