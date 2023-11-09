"""
This module contains the test cases for the api_call function
"""
import pytest
from HC.call import ApiCall

def test_api_call():
    """
    This test case is used to test the api_call function
    """
    api_call = ApiCall()
    status = api_call.api_call('https://www.google.com/', 'GET')
    assert status == 'UP'

def test_api_call_invalid_url():
    """
    This test case is used to test the api_call function with an invalid url
    """
    api_call = ApiCall()
    status = api_call.api_call('https://www.google.com/invalid', 'GET')
    assert status == 'Down'

def test_api_call_invalid_method():
    """
    This test case is used to test the api_call function with an invalid method
    """
    api_call = ApiCall()
    with pytest.raises(SystemExit):
        api_call.api_call('https://www.google.com/', 'INVALID')