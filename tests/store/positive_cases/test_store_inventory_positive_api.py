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
    assert isinstance(json_response, dict), "Response is not a dictionary"
    
    # Verify the keys and types in the inventory response
    for key, value in json_response.items():
        if key in EXPECTED_INVENTORY_KEYS:
            expected_type = EXPECTED_INVENTORY_KEYS[key]
            assert isinstance(value, expected_type), f"Value for key '{key}' is not of type {expected_type.__name__}"
        else:
            logger.warning(f"Unexpected key '{key}' found in inventory response")