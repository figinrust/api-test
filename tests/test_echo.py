import pytest

from tests.conftest import api_urls

def test_get_basic(api_urls):
    response = api_urls['url_get']
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

    data = response.json()
    assert data['args'] == {}

    assert data['url'] == 'https://postman-echo.com/get'
    assert data["headers"]["host"] == 'postman-echo.com'

def test_post_basic(api_urls):
    response = api_urls['url_post']
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

    data = response.json()

    assert data['args'] == {}
    assert data['data'] == {}
    assert data['files'] == {}
    assert data['form'] == {}

    assert data['url'] == 'https://postman-echo.com/post'
    assert data["headers"]["host"] == 'postman-echo.com'

def test_put_basic(api_urls):
    response = api_urls['url_put']
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

    data = response.json()

    assert data['args'] == {}
    assert data['data'] == {}
    assert data['files'] == {}
    assert data['form'] == {}

    assert data['url'] == 'https://postman-echo.com/put'
    assert data["headers"]["host"] == 'postman-echo.com'

def test_get_qwery_parameters_basic(api_urls):
    response = api_urls['url_get_qwery_parameters']
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

    data = response.json()

    assert data['args'] == {
        'foo': 'bar',
        'test': '123'
    }
    assert data['url'] == 'https://postman-echo.com/get?foo=bar&test=123'
    assert data["headers"]["host"] == 'postman-echo.com'

def test_delete_basic(api_urls):
    response = api_urls['url_delete']
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

    data = response.json()

    assert data['args'] == {}
    assert data['data'] == {}
    assert data['files'] == {}
    assert data['form'] == {}

    assert data['url'] == 'https://postman-echo.com/delete'
    assert data["headers"]["host"] == 'postman-echo.com'