import pytest

@pytest.mark.parametrize("username,password", [("sreenu", 123), ("saarya", 321), ("lakshmi", 000)])
def test_login(username, password):
    print("username:", username, "password:", password)

@pytest.mark.parametrize("a,b",[(1,3),(2,4),(5,7),(6,8)])
def test_printabvalues(a,b):
    print(a,b)