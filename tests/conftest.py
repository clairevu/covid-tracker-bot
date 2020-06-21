"""
tests.conftest.py
~~~~~~~~~~~~~~~~~
"""

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from api import main

ROOT = Path(__file__).joinpath("..").joinpath("..").resolve()
TEST_DATA_PATH = ROOT / "tests" / "data"


@pytest.fixture(scope="session")
def test_data_path():
    return TEST_DATA_PATH


@pytest.fixture(scope="session")
def api_client():
    """FastAPI testing client"""
    return TestClient(main.app)


# Test data

with open(str(TEST_DATA_PATH / "messaging_data.json")) as outfile:
    MESSAGING_DATA = json.load(outfile)
    INVALID_MESSAGING_DATA = MESSAGING_DATA.get("invalid")
    VALID_MESSAGING_DATA = MESSAGING_DATA.get("valid")


@pytest.fixture(scope="session", params=VALID_MESSAGING_DATA)
def test_data_valid_messaging(request):
    """Test data for valid messaging models"""
    return request.param


@pytest.fixture(scope="session", params=INVALID_MESSAGING_DATA)
def test_data_invalid_messaging(request):
    """Test data for invalid messaging models"""
    return request.param


with open(str(TEST_DATA_PATH / "message_data.json")) as outfile:
    MESSAGE_DATA = json.load(outfile)
    INVALID_MESSAGE_DATA = MESSAGE_DATA.get("invalid")
    VALID_MESSAGE_DATA = MESSAGE_DATA.get("valid")


@pytest.fixture(scope="session", params=VALID_MESSAGE_DATA)
def test_data_valid_message(request):
    """Test data for valid message models"""
    return request.param


@pytest.fixture(scope="session", params=INVALID_MESSAGE_DATA)
def test_data_invalid_message(request):
    """Test data for invalid message models"""
    return request.param


with open(str(TEST_DATA_PATH / "event_data.json")) as outfile:
    EVENT_DATA = json.load(outfile)
    INVALID_EVENT_DATA = EVENT_DATA.get("invalid")
    VALID_EVENT_DATA = EVENT_DATA.get("valid")


@pytest.fixture(scope="session", params=VALID_EVENT_DATA)
def test_data_valid_event(request):
    """Test data for valid event models"""
    return request.param


@pytest.fixture(scope="session", params=INVALID_EVENT_DATA)
def test_data_invalid_event(request):
    """Test data for invalid event models"""
    return request.param
