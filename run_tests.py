import pytest
import subprocess

if __name__ == "__main__":
    pytest.main(["--html=reports/pytest_report.html", "--self-contained-html"])
    subprocess.run(["behave", "--junit", "--junit-directory=reports/behave"])
