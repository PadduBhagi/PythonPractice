from _ast import *

import pytest

import Practice
class TestCalculations():
    @pytest.mark.sanity
    def test_add(self):
        print("addition method")
    @pytest.mark.smoke
    def test_sub(self):
        print("substract method")
    @pytest.mark.regression
    def test_mul(self):
        print("multiplication method")
    def test_div(self):
        print("division method")
    @pytest.mark.regression
    def test_mod(self):
        print("modulus method")
    @pytest.mark.smoke
    def test_assertion(self):
        a,b=5,10
        print(a,b)



