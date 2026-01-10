import pytest

import Practice
class Test_wishlist():

    def test_wishlist(self):
        print("wishlist method")
    @pytest.mark.skip
    def test_sayHi(self):
        print("Hello")
        assert False
    @pytest.mark.xfail
    def test_sayHello(self):
        print("Hai")