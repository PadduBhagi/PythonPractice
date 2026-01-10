import pytest

from conftest import test_setup_and_teardown


@pytest.mark.usefixtures("test_setup_and_teardown")
class Test_wishlist():

    def test_wishlist(self):
        print("wishlist method")
    @pytest.mark.xfail
    def test_sayHello(self):
        print("Hello")
        assert False
    @pytest.mark.xfail
    def test_sayHai(self):
        print("Hai")