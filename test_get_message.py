import json


def test_get_message(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    name = 'Arojit'
    data = {
        'name': name
    }
    response = client.post('/get-message', data=json.dumps(data), headers=headers)

    assert response.content_type == mimetype
    expected = {
        'message': 'Hello ' + name
    }
    assert expected == json.loads(response.get_data())
