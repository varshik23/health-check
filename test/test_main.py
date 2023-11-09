import pytest
import HC.__main__
from HC.parse import Parse

def test_send_request(monkeypatch):
    parse = Parse()
    urls = parse.parse_yaml('test/mock_data/test_1.yaml')

    def mock_send_request(urls):
        raise KeyboardInterrupt("Simulated KeyboardInterrupt")

    # Monkeypatch the function to use the mock version
    monkeypatch.setattr("HC.__main__.send_requests", mock_send_request)

    with pytest.raises(KeyboardInterrupt):
        HC.__main__.send_requests(urls)
