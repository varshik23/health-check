from collections import defaultdict
import time
import argparse

from HC.parse import Parse
from HC.call import ApiCall

def send_request(urls):
    up_count = defaultdict(int)
    total_calls = defaultdict(int)
    api_call = ApiCall()
    try:
        while True:
            for url, method in urls:
                status = api_call.api_call(url, method)
                domain = url.split("//")[1].split('/')[0]
                if status == "UP":
                    up_count[domain] += 1
                total_calls[domain] += 1
            
            for domain in up_count:
                availability = ( up_count[domain] / total_calls[domain] ) * 100
                print(f"{domain} has {availability}% availability percentage")
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nExiting health check")  

def main():
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
                            help="Enter path to yaml file") 
    args = parsed_args.parse_args()
    parse = Parse()
    urls = parse.parse_yaml(args.path)
    send_request(urls)
    
if __name__ == '__main__':
    main()