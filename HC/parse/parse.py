import yaml
import sys

class Parse:
    def __init__(self):
        self.urls = []

    def parse_yaml(self, path):
        try:
            with open(path, 'r') as f:
                endpoints = yaml.load(f, Loader=yaml.FullLoader)
                for endpoint in endpoints:
                    method = endpoint['method'] if 'method' in endpoint else 'GET'
                    self.urls.append((endpoint['url'], method))
        except FileNotFoundError:
            print('File not found')
            sys.exit(1)
        except yaml.YAMLError as e:
            print(e)
            sys.exit(1)
        return self.urls
