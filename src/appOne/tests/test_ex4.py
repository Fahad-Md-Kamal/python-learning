import pytest


# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")


# @pytest.mark.django_db
# def test_user_create(user_1):

#     user_1.set_password("new-passwords")
#     assert user_1.check_password("new-passwords") is True

# def test_username(user_1):
#     print('check username')
#     assert user_1.username == 'test-user'

def test_set_check_password(new_user):
    print('check-password')
    assert new_user.check_password('password') is True

def test_create_new_user(new_user):
    print(new_user.first_name)
    assert new_user.first_name == 'MyName'

def test_create_new_staff_user(staff_user):
    print(staff_user.is_staff)
    assert staff_user.is_staff == True
