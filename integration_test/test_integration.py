import requests

API_URL = "http://localhost:8000"
UI_URL = "http://localhost:3000"

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
