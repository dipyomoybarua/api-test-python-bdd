from pytest_bdd import given, when, then
from utils.api_client import APIClient
from utils.data_generator import DataGenerator
from utils.logger import logger
from utils.assertions import assert_status_code, assert_response_contains

api_client = APIClient()
data_generator = DataGenerator()

@given('valid order data')
def step_given_valid_order_data(context):
    context.order_data = data_generator.generate_order_data_with_faker()

@when('sending a request to create an order')
def step_when_send_create_order_request(context):
    context.response = api_client.post('order', endpoint_path='/order', data=context.order_data)
    logger.info("Order Data: %s", context.order_data)
    logger.info("Response Status Code: %s", context.response.status_code)
    logger.info("Response Data: %s", context.response.json())

@then('the order creation is successful')
def step_then_order_created_successfully(context):
    assert_status_code(context.response, 200)

@then('the response includes order details')
def step_then_response_contains_order_details(context):
    assert_response_contains(context.response, "petId", context.order_data["petId"])
    assert_response_contains(context.response, "quantity", context.order_data["quantity"])
    assert_response_contains(context.response, "shipDate", context.order_data["shipDate"].replace("Z", "+0000"))
    assert_response_contains(context.response, "status", context.order_data["status"])
    assert_response_contains(context.response, "complete", str(context.order_data["complete"]).lower())
