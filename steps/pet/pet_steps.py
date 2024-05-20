from behave import given, when, then
from utils.api_client import APIClient
from utils.data_generator import DataGenerator
from utils.logger import logger
from utils.assertions import assert_status_code, assert_response_contains

api_client = APIClient()
data_generator = DataGenerator()

@given('a valid pet data')
def step_given_valid_pet_data(context):
    context.pet_data = data_generator.generate_pet_data_with_faker()

@when('sending a request to create a pet')
def step_when_send_create_pet_request(context):
    context.response = api_client.post('pet', data=context.pet_data)
    logger.info("Pet Data: %s", context.pet_data)
    logger.info("Response Status Code: %s", context.response.status_code)
    logger.info("Response Data: %s", context.response.json())

@then('the pet creation is successful')
def step_then_pet_created_successfully(context):
    assert_status_code(context.response, 200)

@then('the response includes pet name and status')
def step_then_response_contains_pet_details(context):
    assert_response_contains(context.response, "name", context.pet_data["name"])
    assert_response_contains(context.response, "status", context.pet_data["status"])
