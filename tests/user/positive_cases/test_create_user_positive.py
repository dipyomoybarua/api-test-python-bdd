import pytest
import json
from utils.api_client import APIClient
from utils.data_generator import DataGenerator
from utils.logger import logger
from utils.assertions import assert_status_code, assert_response_contains

api_client = APIClient()
data_generator = DataGenerator()

def test_create_user():
    user_data = data_generator.generate_user_data()

    response = api_client.request(
        method='post',
        endpoint_key='user',
        endpoint_path='/createWithList',
        data=user_data
    )

    logger.info("User Data: %s", json.dumps(user_data, indent=2))
    logger.info("Response Status Code: %s", response.status_code)
    logger.info("Response Data: %s", response.json())

    assert_status_code(response, 200)

    response_json = response.json()
    for user in user_data:
        assert_response_contains(response_json, "username", user["username"])
        assert_response_contains(response_json, "email", user["email"])
