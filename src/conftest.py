import pytest
from django.contrib.auth.models import User

@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test-user")
    user.set_password("new-passwords")
    print('create-user')
    return user

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
            username:str,
            password:str = None,
            first_name:str = "firstname",
            last_name:str = "lastname",
            email:str = "test@test.com",
            is_staff:bool=False,
            is_superuser:bool=False,
            is_active:bool=True
        ):
        user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_staff=is_staff,
                is_superuser=is_superuser,
                is_active=is_active
            )
        return user

    return create_app_user

@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory("Test-user", "password", "MyName")

@pytest.fixture
def staff_user(db, new_user_factory):
    return new_user_factory("Test-user", "password", "MyName", is_staff=True)