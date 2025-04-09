import requests
import json
import pytest

base_url = "https://gorest.co.in/"
auth_token = "Bearer 77623844a42b24e0f48a62055ebbd789068b57ef4643a6063b3253df5ea8d5c5"

@pytest.mark.skip
def test_create_user():
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}
    body = {
            'name':"Tenali Ramakrishna",
            'email':"tenali.ramakrishna456@gmail.com",
            'gender':"male",
            'status':"active"
            }
    response = requests.post(url, headers=headers, json=body)
    print(response.status_code)
    assert response.status_code == 201

@pytest.mark.skip
def test_get_users():
    url = base_url + "/public/v2/users"
    headers = {"Authorization":auth_token}
    response = requests.get(url,headers=headers)
    print(response)
    assert response.status_code == 200


# @pytest.mark.skip
def test_get_single_user():
    url = base_url + "/public/v2/user/7817037"
    headers = {"Authorization":auth_token}
    response = requests.get(url,headers=headers)
    print(response)
    assert response.status_code == 200
    # json_resp = response.json()
    # print(json_resp)
    # name = "Sen. Atreyi Chattopadhyay"
    # assert json_resp['name'] == name

# get_single_user()
@pytest.mark.skip
def test_modify_user():
    url = base_url + "/public/v2/users/7817037"
    headers = {"Authorization": auth_token}
    body = { 'name': 'Anita Adibatti',
            'email': 'anitaadb@gmail.com',
             'gender': 'female',
            'status': 'active'}
    response = requests.put(url,headers=headers,json=body)
    assert response.status_code == 200

@pytest.mark.skip
def test_delete_user():
    url = base_url + "/public/v2/users/7817026"
    headers = {"Authorization": auth_token}

    response = requests.delete(url,headers=headers)
    assert response.status_code == 204

