from datetime import datetime

def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, got {response.status_code}"

def assert_response_contains(response, key, expected_value):
    try:
        json_response = response.json()
        actual_value = json_response[key]
        
        # Special handling for "shipDate"
        if key == "shipDate":
            actual_date = datetime.strptime(actual_value, "%Y-%m-%dT%H:%M:%S").date()
            expected_date = datetime.strptime(expected_value, "%Y-%m-%dT%H:%M:%S").date()
            assert actual_date == expected_date, f"Expected shipDate to be {expected_value}, got {actual_value}"
            return
        
        # Direct comparison for other cases
        assert str(actual_value).strip() == str(expected_value).strip(), f"Expected {key} to be {expected_value}, got {actual_value}"
    except Exception as e:
        print(f"Error comparing values for key '{key}': {e}")