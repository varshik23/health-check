import requests
import sys

class ApiCall:
    def __init__(self):
        pass

    def api_call(self, url, method):
        try:
            if method == "GET":
                response = requests.get(url)
            elif method == "POST":
                response = requests.post(url)
            elif method == "PUT":
                response = requests.put(url)
            elif method == "DELETE":
                response = requests.delete(url)
            else:
                print("Method not supported")
                sys.exit(1)
            status = "UP"
            if not response.ok or response.elapsed.total_seconds() * 1000 > 500:
                status = "Down"
            return status
        except requests.exceptions.ConnectionError:
            return 404
