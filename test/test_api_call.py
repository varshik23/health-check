import pytest
from HC.call import ApiCall

def test_api_call():
    api_call = ApiCall()
    status = api_call.api_call('https://www.google.com/', 'GET')
    assert status == 'UP'

def test_api_call_invalid_url():
    api_call = ApiCall()
    status = api_call.api_call('https://www.google.com/invalid', 'GET')
    assert status == 'Down'

def test_api_call_invalid_method():
    api_call = ApiCall()
    with pytest.raises(SystemExit):
        api_call.api_call('https://www.google.com/', 'INVALID')