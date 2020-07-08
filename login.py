import pytest

pytest


def test_login():
    print("程序运行")


if __name__ == '__main__':
    pytest.main(["-s", "test_abc.py"])