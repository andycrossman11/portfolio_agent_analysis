from prometheus_client import Counter

# Counter to track requests per endpoint and method
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint"]
)

def track_request(method: str, endpoint: str):
    """Helper to increment request counter"""
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()

def get_request_metrics():
    """Extract current request counts into JSON format"""
    metrics = []
    for label, metric in REQUEST_COUNT._metrics.items():
        method, endpoint = label
        metrics.append({
            "method": method,
            "endpoint": endpoint,
            "count": metric._value.get()  # Get the current value of the counter
        })
    return metrics