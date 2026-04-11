from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidTokenError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Token is invalid or expired')
    default_code = 'invalid_access_token'


class AuthenticationError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Incorrect authentication credentials')
    default_code = 'authentication_failed'
