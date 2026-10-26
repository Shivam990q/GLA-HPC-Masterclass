# solution_day03_all.py
# Working solutions for Day 3 Web Development practice problems

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, EmailStr
from typing import List, Dict
import uvicorn

app = FastAPI(title="Day 3 Web Solutions API")

# In-memory storage
users_db: Dict[int, dict] = {}
user_id_seq = 1

class UserCreate(BaseModel):
    name: str
    email: str
    role: str = "student"

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

@app.post("/users", response_model=UserResponse)
def create_user(u: UserCreate):
    global user_id_seq
    user_data = {"id": user_id_seq, "name": u.name, "email": u.email, "role": u.role}
    users_db[user_id_seq] = user_data
    user_id_seq += 1
    return user_data

@app.get("/users", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 10):
    return list(users_db.values())[skip : skip + limit]

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# WebSocket Broadcast Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"[Broadcast] Client says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    print("[*] Running Day 3 Practice Solutions API on port 8000...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
