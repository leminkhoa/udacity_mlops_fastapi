import json
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test__get_return_200():
    '''Test local GET method, should return 200 and Hello World message'''
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello World!"}


def test__post_return_200():
    '''Test local POST method, should return 200 and predicted salary'''
    input = {
        "age": 25,
        "workclass": "Federal-gov",
        "fnlgt": 35,
        "education": "Bachelors",
        "education_num": 13,
        "marital_status": "Divorced",
        "occupation": "Farming-fishing",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital_gain": 0,
        "capital_loss": 0,
        "hours_per_week": 15,
        "native_country": "United-States"
    }
    data = json.dumps(input)
    r = client.post("/inferences/", data=data)
    assert r.status_code == 200
    assert r.json()['pred_salary'] in ['<=50K', '>50K']


def test__post_empty_input_return_422():
    '''Test local POST method from empty body, should return 422'''
    input = dict()
    data = json.dumps(input)
    r = client.post("/inferences/", data=data)
    assert r.status_code == 422


def test__post_missing_fields_return_500():
    '''Test local POST method with body having wrong schema, should return 500'''
    input = {
        "age": 25,
    }
    data = json.dumps(input)
    r = client.post("/inferences/", data=data)
    assert r.status_code == 500
