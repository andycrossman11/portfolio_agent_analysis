import pytest
import requests
import time

API_URL = "http://localhost:8000/"
UI_URL = "http://localhost:3000"

@pytest.fixture(scope="session", autouse=True)
def wait_for_services():
    # Wait until API is healthy
    timeout = time.time() + 60  # 60 seconds timeout
    while time.time() < timeout:
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                print("✅ API is up")
                break
        except requests.ConnectionError:
            pass
        time.sleep(5)
    else:
        pytest.fail("❌ API did not become healthy in time")

def test_ui_available():
    response = requests.get(UI_URL)
    assert response.status_code == 200

def test_api_health():
    response = requests.get(f"{API_URL}/health")
    assert response.status_code == 200

def test_api_get_positions():
    response = requests.get(f"{API_URL}/positions")
    assert response.status_code == 200

def test_api_get_analysis():
    response = requests.get(f"{API_URL}/analysis")
    assert response.status_code == 200

def test_api_get_perf_metrics():
    response = requests.get(f"{API_URL}/performance/endpoint_metrics")
    assert response.status_code == 200
