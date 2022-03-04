- RUN pytest:
```sh
pytest
```

- Run Pytest with Report
```sh
pytest -rP
```

- Run Pytest of a specific folder or test function
```sh
pytest appOne/tests/test_ex1.py::test_example1
```
- Use Marks to identify test with specific test
```python
@pytest.mark.skip
def test_example1():
    assert 1 == 1
```
***Command***
```sh
pytest -m skip
```

**Fixture with Factory**
- Create a ```conftest.py``` python file
- **PyTest** calls all the fixtures from ```conftest.py``` file before reading any tests. **N.B.** Therefore it doesn't requrie to import fixture funtions of another python file from test functions.
- Add the functions to the file
- Add User Creation function

```python
# /conftest.py

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
```
<br>

- Create user using the factory
```python
# /conftest.py

@pytest.fixture
def staff_user(db, new_user_factory):
    return new_user_factory("Test-user", "password", "MyName", is_staff=True)
```

- Call the fixture from test functions by just passing the fixture function as param.
```python
# /test_ex4.py

def test_set_check_password(new_user):
    print('check-password')
    assert new_user.check_password('password') is True

def test_create_new_user(new_user):
    print(new_user.first_name)
    assert new_user.first_name == 'MyName'

def test_create_new_staff_user(staff_user):
    print(staff_user.is_staff)
    assert staff_user.is_staff == True
```
