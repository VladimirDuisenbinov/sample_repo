from django.test import Client

from url_short.tests.fixtures import url_short
from url_short.models import URLShort
from url_short.repos import URLShortRepo

URL = '/url-shorts'

def test_get_all_url_shorts_200(
    db,
    client: Client,
    url_short: URLShort
):
    response = client.get(path=f'{URL}/')

    assert 200 == response.status_code and response.json() == {
        'status': 'success',
        'data': [
            {
                'id': url_short.pk,
                'url': url_short.url,
                'short_url': url_short.short_url
            }
        ]
    }

def test_get_no_url_shorts_200(
    db,
    client: Client
):
    response = client.get(path=f'{URL}/')

    assert 200 == response.status_code and response.json() == {
        'status': 'success',
        'data': []
    }

def test_retrieve_url_short_200(
    db,
    client: Client,
    url_short: URLShort
):
    response = client.get(path=f'{URL}/{url_short.pk}/')

    assert 200 == response.status_code and response.json() == {
        'status': 'success',
        'data': {
                'id': url_short.pk,
                'url': url_short.url,
                'short_url': url_short.short_url
        }
    }

def test_retrieve_url_short_404(
    db,
    client: Client
):
    response = client.get(path=f'{URL}/1/')

    assert 404 == response.status_code and response.json() == {
        'status': 'error',
        'error': {
            'message': 'Not found.',
            'type': 'NOT_FOUND'
        }
    }

def test_update_url_short_202(
    db,
    client: Client,
    url_short: URLShort
):
    new_url = 'http://non_existing_url.com'

    response = client.patch(
        path=f'{URL}/{url_short.pk}/',
        content_type='application/json',
        data={
            'url': new_url
        }
    )

    assert 202 == response.status_code and response.json() == {
        'status': 'success',
        'data': {
            'id': url_short.pk,
            'url': new_url,
            'short_url': url_short.short_url
        } 
    }

def test_update_url_short_400(
    db,
    client: Client,
    url_short: URLShort
):
    new_url = 'http://example.com'
    instance = URLShortRepo.create({'url': new_url})

    response = client.patch(
        path=f'{URL}/{url_short.pk}/',
        content_type='application/json',
        data={
            'url': new_url
        }
    )

    assert 400 == response.status_code and response.json() == {
        'status': 'error',
        'error': {
            'message': 'url: This field must be unique.',
            'type': 'INTERNAL_SERVER_ERROR'
        }
    }

def test_create_url_short_201(
    db,
    client: Client,
    url_short: URLShort
):
    free_url = 'http://free_url.com'

    response = client.post(
        path=f'{URL}/',
        content_type='application/json',
        data={
            'url': free_url
        }
    )

    assert 201 == response.status_code

def test_create_url_short_400(
    db,
    client: Client,
    url_short: URLShort
):
    busy_url = url_short.url

    response = client.post(
        path=f'{URL}/',
        content_type='application/json',
        data={
            'url': busy_url
        }
    )

    assert 400 == response.status_code and response.json() == {
        'status': 'error',
        'error': {
            'message': 'url: This field must be unique.',
            'type': 'INTERNAL_SERVER_ERROR'
        }
    }

def test_delete_url_short_204(
    db,
    client: Client,
    url_short: URLShort
):
    response = client.delete(
        path=f'{URL}/{url_short.pk}/',
        content_type='application/json'
    )

    assert 204 == response.status_code

def test_delete_url_short_400(
    db,
    client: Client
):
    response = client.delete(
        path=f'{URL}/10/',
        content_type='application/json'
    )

    assert 404 == response.status_code and response.json() == {
        'status': 'error',
        'error': {
            'message': 'Not found.',
            'type': 'NOT_FOUND'
        }
    }
