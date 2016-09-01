from jupyterhub.auth import Authenticator, LocalAuthenticator

from tornado import gen


class DummyAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        return data['username']

class LocalDummyAuthenticator(LocalAuthenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        return data['username']
