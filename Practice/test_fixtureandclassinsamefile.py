import pytest
from selenium import webdriver
@pytest.fixture()
def test_setup_and_teardown():
    print("launch appliaction")
    print("click on login")
    print("loginto app")
    yield
    print("logout from app")

def test_a(test_setup_and_teardown):
    print("method a")
def test_b(test_setup_and_teardown):
    print("method b")
def test_c():
    print("method c")




