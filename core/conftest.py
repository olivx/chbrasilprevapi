import pytest
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APIRequestFactory


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def django_request():
    request_factory = APIRequestFactory()
    return request_factory.get("/")


@pytest.fixture()
def token():
    email = "emailtest@email.com"
    password = "logan$2340OOOO"
    User = get_user_model()
    if not User.objects.filter(email=email).exists():
        user = User.objects.create_user(email=email, password=password)
    user = User.objects.filter(email="emailtest@email.com").first()

    token = Token.objects.filter(user__email=email).first()
    if not Token.objects.filter(user__email=email).first():
        token = Token.objects.create(**{"user": user})
    return token
