import pytest
import requests

@pytest.fixture
def api_urls():
    return {
        'url_get': requests.get("https://postman-echo.com/get"),
        'url_post': requests.post("https://postman-echo.com/post"),
        'url_put': requests.put("https://postman-echo.com/put"),
        'url_get_qwery_parameters': requests.get("https://postman-echo.com/get?foo=bar&test=123"),
        'url_delete': requests.delete("https://postman-echo.com/delete"),
    }
