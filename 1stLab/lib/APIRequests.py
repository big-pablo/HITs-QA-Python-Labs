import requests

BASE_URL = 'http://127.0.0.1:5000'


def get_form():
    response = requests.get(BASE_URL)
    return response


def post_form(coins, amount):
    post_data = {'coins': coins, 'amount': amount}
    response = requests.post(BASE_URL, data=post_data)
    return response
