import requests

def test_get_categories():
    res = requests.get('http://localhost:5000/categories')
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_songs():
    res = requests.get('http://localhost:5000/songs', params={'category': '00년대'})
    assert res.status_code == 200
    assert isinstance(res.json(), list)
