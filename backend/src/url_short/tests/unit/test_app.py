from url_short.apps import UrlShortConfig

def test_app():
    assert UrlShortConfig.name == 'url_short'
