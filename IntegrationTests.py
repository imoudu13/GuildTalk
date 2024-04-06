import pytest
from unittest.mock import patch
from app import app


@pytest.fixture
def client():
    # Create a test client using the Flask application
    with app.test_client() as client:
        yield client


# Mocking the database interaction
@patch('app.db')
def test_login(mock_db, client):
    # Mock the retrieve_document method to return a user
    mock_user = {'username': 'test_user', 'password': 'password'}
    mock_db.retrieve_document.return_value = mock_user

    # Test login functionality
    response = client.post('/', data={'username': 'test_user', 'password': 'password'}, follow_redirects=True)
    assert b'Login' in response.data
    assert b'Login unsuccessful' not in response.data


@patch('app.db')
def test_register(mock_db, client):
    # Mock the create_user method
    mock_db.create_user.return_value = True

    # Test registration functionality
    response = client.post('/register', data={'firstname': 'Test', 'lastname': 'User', 'username': 'test_user',
                                              'email': 'test@example.com', 'password': 'password'},
                           follow_redirects=True)
    assert b'Registration' in response.data


@patch('app.db')
def test_profile(mock_db, client):
    # Mock the retrieve_document method to return user information
    mock_user = {'first': 'Test', 'last': 'User', 'email': 'test@example.com', 'password': 'pw'}
    mock_db.retrieve_document.return_value = mock_user

    # Test profile page functionality
    with client.session_transaction() as sess:
        sess['username'] = 'test_user'
    response = client.get('/profile')
    assert b'Test User' in response.data
    assert b'test@example.com' in response.data


@patch('app.db')
def test_add_channel(mock_db, client):
    mock_db.retrieve_document.return_value = {'users': ['test_user'], 'admins': ['admin']}
    mock_db.update.return_value = None

    response = client.post('/channel', json={'channelName': 'test_channel'}, follow_redirects=True)

    assert response.status_code == 200
    assert b'Channel added successfully' in response.data


@patch('app.session', {'username': 'test_user'})
@patch('app.db')
def test_send_message(mock_db, client):
    mock_db.retrieve_document.return_value = {'users': ['test_user'], 'admins': ['admin']}
    mock_db.update.return_value = None

    response = client.post('/channel', json={'text': 'Hello', 'curr_channel': 'test_channel'}, follow_redirects=True)

    assert response.status_code == 200
    assert b'Message added successfully' in response.data

