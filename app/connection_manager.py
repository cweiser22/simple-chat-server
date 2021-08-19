from fastapi import WebSocket
from typing import List


# ConnectionManager keeps track of connections and encapsulates basic functions
class ConnectionManager:

    def __init__(self):
        # list of all active connections
        self.active_connections: List[WebSocket] = []

    # called whenever a new client connects
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    # called whenever a client disconnects
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    """
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json({
            "event": "pm",
            "data": message
        })
        """

    # sends a message to all sockets
    # all messages are JSON data with two properties, event and data
    # event specifies the action, and data contains any associated info
    async def broadcast(self, event: str, data: any):
        for connection in self.active_connections:
            await connection.send_json({
                "event": event,
                "data": data
            })
