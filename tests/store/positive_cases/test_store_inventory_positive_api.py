import pytest
from utils.api_client import APIClient
from utils.assertions import assert_status_code
from utils.inventory_keys import EXPECTED_INVENTORY_KEYS
import logging

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Instantiate the APIClient
api_client = APIClient()

def test_get_inventory():
    # Send GET request to inventory endpoint
    response = api_client.request('get', 'order', '/inventory')
    
    # Log details
    logger.info("Response Status Code: %s", response.status_code)
    logger.info("Response Data: %s", response.json())
    
    # Assertions
    assert_status_code(response, 200)

    # Verify the response is a dictionary
    json_response = response.json()
    assert type(json_response) == dict, "Response is not a dictionary"


    # Verify that all expected keys are present and have integer values
    for key, value_type in EXPECTED_INVENTORY_KEYS.items():
        assert key in json_response, f"Key '{key}' not found in inventory response"
        assert isinstance(json_response[key], value_type), f"Value for key '{key}' is not of type {value_type.__name__}"
