from rest_framework import authentication
from rest_framework.authtoken.models import Token

from account.models import User


class DevAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        return None
