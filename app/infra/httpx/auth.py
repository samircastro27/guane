from httpx._auth import Auth


class BearerAuth(Auth):
    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
        request.headers["authorization"] = "Bearer " + self.token
        yield request
