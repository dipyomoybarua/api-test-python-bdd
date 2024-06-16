API Test Framework:-

This is the testing framework for **https://petstore.swagger.io/** using Behave for BDD and pytest for unit tests.

Directory Structure:- 

**config/**: Configuration files for different environments.

**features/**: Feature files and step definitions for Behave.

**tests/**: Unit tests using pytest.

**utils/**: Utility functions and classes.

**reports/**: Directory for test reports.

**run_tests.py**: Script to run all tests.

**Setup**:-

Now clone the repository.
Install the dependencies:** pip install -r requirements.txt**
Set the python path for the powershell :- **$env:PYTHONPATH=E:\path\to\your\project\api_test_framework:PYTHONPATH"**
Run the tests using the following command:** pytest tests/ --html=reports/pytest_report.html --self-contained-html**

**Configuration**:-

The configuration file `**config/config.yaml**` includes the base URL, headers, and endpoints:-
```yaml
api_base_url: "https://petstore.swagger.io/v2"
headers:
  accept: "application/json"
  Content-Type: "application/json"
endpoints:
  pet: "/pet"
  order: "/store"
  user: "/user"
