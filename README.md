# Simple Chat Room Server

This is an incredibly basic chat room server. There is one chat room and it transmits only basic text.

## Endpoints
The server has one main endpoint, `/ws/{username}`, where `username` is a string chosen by the user.

## Events
Events sent from the server follow a simple format. Each event is a JSON object with two properties: `event` and `data`.
- `event` is a string that identifies the type of action that is being broadcast
- `data` is any additional data associated with the message. For now, data will either be an object or a string.

### Event Types
- `user_joined` is sent when a new user enters the room. It's `data` is the new user's username as a string.
- `user_left` is sent when a user leaves. It's `data` is the username of the user that left as a string.
- `new_message` is sent when a user sends a message. It's `data` is an object with properies `sent_by` and `text`, both of which are strings.

## Run locally
To run this project, make sure you have virtualenv installed.
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app
```

Visit [localhost:8080](http://localhost:8080) in your browser to make sure it worked.

# Run with Docker

```
docker build -t <container_name> .
docker run -dp 8080:8080 <container_name>
```

Visit [localhost:8080](http://localhost:8080) in your browser to make sure it's running properly.