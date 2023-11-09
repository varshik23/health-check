import pytest
from HC.parse import Parse

def test_parse():
    parse = Parse()
    urls = parse.parse_yaml('test/mock_data/test_1.yaml')
    assert urls == [('https://www.google.com/', 'GET'), ('https://www.yahoo.com/', 'GET')]

def test_parse_empty_method():
    parse = Parse()
    urls = parse.parse_yaml('test/mock_data/test_2.yaml')
    assert urls == [('https://fetch.com/', 'POST'), ("https://fetch.com/careers", "PUT"),
                    ("https://fetch.com/rewards", "GET")]

def test_invalid_path():
    parse = Parse()
    with pytest.raises(SystemExit):
        parse.parse_yaml('test/mock_data/test_3.yaml')
    