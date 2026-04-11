import uuid

import pytest

from .test_helpers import ExtAPIClient


@pytest.fixture
def create_user(django_user_model):
    def make_user(**kwargs):
        kwargs['password'] = '123456'
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def api_client():
    return ExtAPIClient()
