import pytest
from helloworld import hello

# @pytest.mark.hello
def test_hello():
    result = hello()
    assert result == 'Hello Khaoula !'