from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.connection_manager import ConnectionManager

# main FastAPI app
app = FastAPI()

# create our connection manager
manager = ConnectionManager()


@app.get("/")
def index():
    return "You are at the root endpoint :)."


# main websocket endpoint
@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    print("endpoint")
    await manager.broadcast("new_member", username)

    try:
        while True:
            data = await websocket.receive_text()

            await manager.broadcast("new_message", {
                "sent_by": username,
                "text": data
            })

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("user_left", username)
