import pytest
from core.user.models import User
# Create your tests here.

data_user = {
    "username": "Lebron_James",
    "first_name": "Lebron",
    "last_name": "James",
    "email": "lebronjames@gmail.com",
    "phone_number": "0733559395",
    "password": "qwertyuiop"
}

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(**data_user)
    assert user.username == data_user["username"]
    assert user.first_name == data_user["first_name"]
    assert user.last_name == data_user["last_name"]
    assert user.email == data_user["email"]
    assert user.phone_number == data_user["phone_number"]
