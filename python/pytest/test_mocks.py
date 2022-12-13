from pathlib import Path
import requests




def getssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"


def test_getssh(monkeypatch):
    # mocked return function to replace Path.home
    # always return '/abc'
    def mockreturn():
        return Path("/abc")
    # Application of the monkeypatch to replace Path.home
    # with the behavior of mockreturn defined above.
    # monkeypatch.setattr(Path, "home", mockreturn)
    monkeypatch.setattr("pathlib.Path.home", lambda: Path("/abc"))
    # Calling getssh() will use mockreturn in place of Path.home
    # for this test with the monkeypatch.
    x = getssh()
    assert x == Path("/abc/.ssh")


def get_json(url):
    """Takes a URL, and returns the JSON."""
    r = requests.get(url)
    return r.json()

class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_json(monkeypatch):
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()
    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)
    # app.get_json, which contains requests.get, uses the monkeypatch
    result = get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"



# # custom class to be the mock return value of requests.get()
# class MockResponse:
#     @staticmethod
#     def json():
#         return {"mock_key": "mock_response"}
# # monkeypatched requests.get moved to a fixture
# @pytest.fixture
# def mock_response(monkeypatch):
#     """Requests.get() mocked to return {'mock_key':'mock_response'}."""
#     def mock_get(*args, **kwargs):
#         return MockResponse()
#     monkeypatch.setattr(requests, "get", mock_get)
# # notice our test uses the custom fixture instead of monkeypatch directly
# def test_get_json(mock_response):
#     result = app.get_json("https://fakeurl")
#     assert result["mock_key"] == "mock_response"



# contents of app.py to generate a simple connection string
DEFAULT_CONFIG = {"user": "user1", "database": "db1"}
def create_connection_string(config=None):
    """Creates a connection string from input or defaults."""
    config = config or DEFAULT_CONFIG
    return f"User Id={config['user']}; Location={config['database']};"

import pytest 

def test_missing_user(monkeypatch):
    # patch the DEFAULT_CONFIG t be missing the 'user' key
    monkeypatch.delitem(DEFAULT_CONFIG, "user", raising=False)
    # Key error expected because a config is not passed, and the
    # default is now missing the 'user' entry.
    with pytest.raises(KeyError):
        _ = create_connection_string()