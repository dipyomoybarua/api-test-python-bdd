from utils.api_client import APIClient
from utils.data_generator import DataGenerator
from utils.assertions import assert_status_code, assert_response_contains

api_client = APIClient()
data_generator = DataGenerator()

def test_create_pet():
    pet_data = data_generator.generate_pet_data_with_faker()
    response = api_client.request('post', 'pet', data=pet_data)
    assert_status_code(response, 200)
    assert_response_contains(response, "name", pet_data["name"])
    assert_response_contains(response, "status", pet_data["status"])