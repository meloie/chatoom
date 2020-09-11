# Chatoom

A simple but sacalable chat room server writen to practice [Starlette](https://github.com/encode/starlette), Redis Pub-Sub and Websockets.

## How to use
- Run:
```bash
docker-compose up
```
- You can use any websocket client to use, for example with [wsdump](https://github.com/websocket-client/websocket-client):
```bash
wsdump.py --headers 'Authorization:Custom <username>' ws://localhost:8000/ws
```
and change *<username>* to your desired username (username must have no spaces)
