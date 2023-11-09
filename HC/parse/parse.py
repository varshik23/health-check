"""
This module is responsible for parsing the yaml file and returning a list of tuples
"""
import yaml
import sys

class Parse:
    """
    This class contains the method parse_yaml which is used to parse the yaml file
    """
    def __init__(self):
        """
        This method is used to initialize the urls list
        """
        self.urls = []

    def parse_yaml(self, path):
        """
        This method is used to parse the yaml file
        :param path: Path of the yaml file
        :return: List of tuples containing the urls, methods and bodies
        """
        try:
            with open(path, 'r') as f: # Open the yaml file
                endpoints = yaml.load(f, Loader=yaml.FullLoader) # Load the yaml file
                for endpoint in endpoints: # Iterate through the endpoints
                    # Check if the method is specified, if not, the default method is GET
                    method = endpoint['method'] if 'method' in endpoint else 'GET' 
                    body = None # Initialize the body to None
                    if method == 'POST' or method == "PUT":
                        # If the method is POST or PUT, check if the body is specified
                        body = endpoint['body'] if 'body' in endpoint else None
                    self.urls.append((endpoint['url'], method, body)) # Append the url, method and body
        except FileNotFoundError: # If the file is not found, exit the program
            print('File not found')
            sys.exit(1)
        except yaml.YAMLError as e: # If there is an error in the yaml file, exit the program
            print(e)
            sys.exit(1)
        return self.urls # Return the list of tuples
