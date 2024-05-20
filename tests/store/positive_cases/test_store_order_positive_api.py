from utils.api_client import APIClient
from utils.data_generator import DataGenerator
from utils.assertions import assert_status_code, assert_response_contains

api_client = APIClient()
data_generator = DataGenerator()

def test_create_order():
    order_data = data_generator.generate_order_data_with_faker()
    response = api_client.request('post', 'order', endpoint_path='/order', data=order_data)
    assert_status_code(response, 200)
    assert_response_contains(response, "id", str(order_data["id"]))  # Assuming order ID is in response
    assert_response_contains(response, "quantity", str(order_data["quantity"]))
    assert_response_contains(response, "shipDate", str(order_data["shipDate"]).replace("Z", "+0000"))
    assert_response_contains(response, "status", order_data["status"])
    assert_response_contains(response, "complete", str(order_data["complete"]).lower())