"""
This module contains the class ApiCall which is used to make the API calls
"""
import requests
import sys

class ApiCall:
    """
    This class contains the method api_call which is used to make the API calls
    """
    def __init__(self):
        pass

    def api_call(self, url, method, body):
        """
        This method is used to make the API calls
        :param url: URL of the API
        :param method: Method of the API
        :param body: Body of the API
        :return: Status of the API
        """
        try: 
            # Check if the method is supported
            if method == "GET": 
                response = requests.get(url)
            elif method == "POST":
                response = requests.post(url, json = body)
            elif method == "PUT":
                response = requests.put(url, json = body)
            elif method == "DELETE":
                response = requests.delete(url)
            else:
                print("Method not supported") # If the method is not supported, exit the program
                sys.exit(1)
            status = "UP" # If the response is ok and the response time is less than 500ms, the status is UP
            if not response.ok or response.elapsed.total_seconds() * 1000 > 500:
                # If the response is not ok or the response time is more than 500ms, the status is Down
                status = "Down"
            return status # Return the status
        except requests.exceptions.ConnectionError: # If the connection is refused, return 404
            return 404
