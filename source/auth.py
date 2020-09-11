
from starlette.authentication import AuthenticationBackend, SimpleUser, AuthenticationError, AuthCredentials
import logging

logger = logging.getLogger(__name__)

class DummyAuthenitcation(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return
        auth = request.headers["Authorization"]
        try:
            scheme, username = auth.split()
            if scheme.lower() != 'custom':
                return
        except Exception as exc:
            logger.debug(f'get exception: {exc}')
            raise AuthenticationError("Bad auth header")
        return AuthCredentials(["authenticated"]), SimpleUser(username)








