import pytest

@pytest.mark.slow
def test_example1():
    assert 1 == 1

@pytest.mark.skip
def test_example2():
    assert 1 == 1