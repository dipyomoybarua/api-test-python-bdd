import json
from behave import given, when, then
from utils.api_client import APIClient
from utils.data_generator import DataGenerator
from utils.logger import logger
from utils.assertions import assert_status_code, assert_response_contains

api_client = APIClient()
data_generator = DataGenerator()

@given('a list of user data')
def step_given_list_of_user_data(context):
    context.user_data = data_generator.generate_user_data()

@when('sending a request to create users with the list')
def step_when_send_create_users_request(context):
    context.response = api_client.request(
        method='post',
        endpoint_key='user',
        endpoint_path='/createWithList',
        data=context.user_data
    )
    logger.info("User Data: %s", json.dumps(context.user_data, indent=2))
    logger.info("Response Status Code: %s", context.response.status_code)
    logger.info("Response Data: %s", context.response.json())

@then('the users are created successfully')
def step_then_users_created_successfully(context):
    assert_status_code(context.response, 200)

@then('the response contains the correct user details')
def step_then_response_contains_user_details(context):
    response_json = context.response.json()
    for user in context.user_data:
        assert_response_contains(response_json, "username", user["username"])
        assert_response_contains(response_json, "email", user["email"])
