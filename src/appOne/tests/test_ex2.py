# import pytest

# # @pytest.fixture
# # def fixture_1():
# #     print('run-fixture-1')
# #     return 1

# # @pytest.fixture(scope='session')
# # def fixture_1():
# #     """
# #         By Default fixtures run once for each tests.
# #         adding (scope='session') will make the fixture to run only once through out the whole session.
# #     """
# #     print('run-fixture-1')
# #     return 1

# @pytest.fixture(scope='session')
# def fixture_1():
#     """
#         By Default fixtures run once for each tests.
#         adding (scope='session') will make the fixture to run only once through out the whole session.
#     """
#     print('Test start')
#     yield 1
#     print('Test End')

# def test_example1(fixture_1):
#     print('run-test_example-1')
#     num = fixture_1
#     assert num == 1

# def test_example2(fixture_1):
#     print('run-test_example-2')
#     num = fixture_1
#     assert num == 1