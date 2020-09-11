from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.routing import Route, WebSocketRoute

from .endpoints import chat_room
from .auth import DummyAuthenitcation

routes = [
    WebSocketRoute("/ws", chat_room),
]

middlewares = [
    Middleware(AuthenticationMiddleware, backend=DummyAuthenitcation()),
]

app = Starlette(debug=True, routes=routes, middleware=middlewares)
