from behave import given, when, then
from utils.api_client import APIClient
from utils.logger import logger
from utils.assertions import assert_status_code

api_client = APIClient()

@given('the store inventory endpoint')
def step_given_inventory_endpoint(context):
    context.endpoint = 'order'
    context.endpoint_path = '/inventory'

@when('sending a request to get store inventory')
def step_when_send_inventory_request(context):
    context.response = api_client.get(context.endpoint, context.endpoint_path)
    logger.info("Response Status Code: %s", context.response.status_code)
    logger.info("Response Data: %s", context.response.json())

@then('the inventory retrieval is successful')
def step_then_inventory_retrieved_successfully(context):
    assert_status_code(context.response, 200)