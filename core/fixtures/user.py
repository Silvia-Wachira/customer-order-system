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

@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data_user) 
