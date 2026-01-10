import pytest
from conftest import get_environment

@pytest.mark.env
def test_environmentselection(get_environment):
    if get_environment == "dev":
        print("dev env")
    elif get_environment == "uat":
        print("uat env")
    elif get_environment == "stage":
        print("stage env")
    else:
        print("qa environment")

