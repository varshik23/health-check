"""
This module is the entry point for the health check application
"""
from collections import defaultdict
import time
import argparse

from HC.parse import Parse
from HC.call import ApiCall

def send_requests(urls):
    """
    This method is used to send the requests to the endpoints
    :param urls: List of tuples containing the urls, methods and bodies
    """
    up_count = defaultdict(int) # Initialize the up_count dictionary
    total_calls = defaultdict(int) # Initialize the total_calls dictionary
    api_call = ApiCall() # Initialize the ApiCall class
    try:
        # Run the health check every 15 seconds
        while True:
            for url, method, body in urls:
                status = api_call.api_call(url, method, body) # Get the status of the API
                domain = url.split("//")[1].split('/')[0] # Get the domain of the API
                if status == "UP":
                    up_count[domain] += 1 # Increment the up_count if the status is UP
                total_calls[domain] += 1 # Increment the total_calls

            for domain in up_count: # Iterate through the domains
                # Calculate the availability percentage
                availability = ( up_count[domain] / total_calls[domain] ) * 100
                # Print the availability percentage
                print(f"{domain} has {availability:.0f}% availability percentage")
            time.sleep(15)
    except KeyboardInterrupt: # If the user presses Ctrl+C, exit the program
        print("\nExiting health check")

def main():
    """
    This method is the entry point for the health check application
    """
    parsed_args = argparse.ArgumentParser(description=
                                          """
                                          Health Check - 
                                          Provides the availability percentage of
                                          the HTTP endpoints
                                          """,
                                          usage = "%(prog)s [options] path",
                                          epilog=
                                          """
                                          Example: %(prog)s input.yaml,
                                          %(prog)s /Users/{user}/Code/health-check/input2.yaml
                                          """) # Initialize the parser
    parsed_args.add_argument("path", metavar="path", type=str,
                            help="Enter path to yaml file") # Add the path argument
    args = parsed_args.parse_args() # Parse the arguments
    parse = Parse() # Initialize the Parse class
    urls = parse.parse_yaml(args.path) # Parse the yaml file
    send_requests(urls) # Send the requests to the endpoints

if __name__ == '__main__':
    main() # Call the main method
