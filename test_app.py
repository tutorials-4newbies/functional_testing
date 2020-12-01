import os

import pytest
import server
from config import Config


@pytest.fixture
def client():
    """
    this is a test fixture
    pytest automagically injects those fixture into test functions if you use their name
    as an argument
    """

    test_db_name = "test.db"
    test_db_path = f"sqlite:///{test_db_name}"
    # We are creating test Config with a specific db
    test_config = Config(database_uri=test_db_path)
    app = server.create_app(test_config)

    app.config['TESTING'] = True  # flask has some configurations happening when this is True,
    # mainly better exception stack traces
    client = app.test_client()
    app.db.create_all()
    #  This client is the part injected into test functions demanding this fixture as an argument
    yield client
    # Yield is a key word you don't know yet - it's a generator, we won't discuss this now
    # Oh, what is this? this code would run "after" the test would finish, so a good place for a teardown
    # Put a breakpoint here and check the file system, before and after
    os.unlink(test_db_name)


def test_howdy(client):
    res = client.get('/howdy')
    assert 'howdy' in str(res.data)


def test_health_endpoint(client):
    res = client.get('/health')
    json_data = res.get_json()
    assert json_data == {"status": "ok"}


def test_parameterized_endpoint(client):
    res = client.get("/goodbye/trump")
    json_data = res.get_json()
    assert json_data == {"response": "goodbye Mr trump"}
