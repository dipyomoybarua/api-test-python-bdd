import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient()
