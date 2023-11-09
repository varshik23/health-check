"""
Test cases for parse.py
"""
import pytest
from HC.parse import Parse

def test_parse():
    """
    This test case is used to test the parse function
    """
    parse = Parse()
    urls = parse.parse_yaml('test/mock_data/test_1.yaml')
    assert urls == [('https://www.google.com/', 'GET', None), ('https://www.yahoo.com/', 'GET', None)]

def test_parse_empty_method():
    """
    This test case is used to test the parse function with an empty method
    """
    parse = Parse()
    urls = parse.parse_yaml('test/mock_data/test_2.yaml')
    body = '{"foo": "bar"}'
    assert urls == [('https://fetch.com/', 'POST', body), ("https://fetch.com/careers", "PUT", body),
                    ("https://fetch.com/rewards", "GET", None)]

def test_invalid_path():
    """
    This test case is used to test the parse function with an invalid path
    """
    parse = Parse()
    with pytest.raises(SystemExit): # Check if the SystemExit is raised
        parse.parse_yaml('test/mock_data/test_3.yaml')
