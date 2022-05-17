from pytest import fixture

from url_short.models import URLShort
from url_short.repos import URLShortRepo


@fixture
def url_short() -> URLShort:
    return URLShortRepo.create({'url': 'http://test_url.com'})
