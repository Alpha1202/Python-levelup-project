def test_get_todos_succeeds(client):
    response = client.get('/to-do')
    assert response.status_code == 200
