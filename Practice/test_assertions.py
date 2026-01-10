

from _ast import *

import pytest

import Practice
class TestCalculations():
    @pytest.mark.sanity
    def test_add(self):
        print("addition method")
    def test_sub(self):
        print("substract method")

    def test_assertion(self):
        a = 5
        b = 10
        assert a > b, "a is less than b"
    @pytest.mark.regression
    def test_mul(self):
        print("multiplication method")
    def test_div(self):
        print("division method")
    @pytest.mark.regression
    def test_mod(self):
        print("modulus method")




