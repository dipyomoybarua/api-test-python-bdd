import yaml
import requests

class APIClient:
    def __init__(self):
        with open("config/config.yaml", 'r') as file:
            config = yaml.safe_load(file)
            self.base_url = config['api_base_url']
            self.headers = config['headers']
            self.endpoints = config['endpoints']

    def request(self, method, endpoint_key, endpoint_path='', data=None, params=None):
        url = f"{self.base_url}{self.endpoints[endpoint_key]}{endpoint_path}"
        try:
            if method.lower() == 'get':
                response = requests.get(url, params=params, headers=self.headers)
            elif method.lower() == 'post':
                response = requests.post(url, json=data, headers=self.headers)
            elif method.lower() == 'put':
                response = requests.put(url, json=data, headers=self.headers)
            elif method.lower() == 'delete':
                response = requests.delete(url, headers=self.headers)
            else:
                raise ValueError("Invalid HTTP method. Supported methods: GET, POST, PUT, DELETE")
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response
        except requests.RequestException as e:
            raise requests.RequestException(f"Error making {method.upper()} request to {url}: {e}")
