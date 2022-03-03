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