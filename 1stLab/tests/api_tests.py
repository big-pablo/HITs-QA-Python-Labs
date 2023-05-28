import pytest
from lib.APIRequests import *


class TestClass:

    def test_get_form_http_status(self):
        assert get_form().status_code == 200

    def test_coin_change_with_reachable_sum(self):
        assert post_form('85 89 7', 431).text == '17'

    def test_coin_change_with_impossible_coins_combination(self):
        assert post_form('2 5 10 12', 3).text == '-1'

    def test_coin_change_with_minimum_amount_possible(self):
        assert post_form('1 12 5', 0).text == '0'

    def test_coin_change_with_no_coins_input(self):
        assert post_form('', 12).status_code == 500

    def test_coin_change_with_too_much_coins(self):
        assert post_form('1 2 3 4 5 6 7 8 9 10 11 12 13', 1).status_code == 500

    def test_coin_change_with_negative_coin(self):
        assert post_form('-1 4', 3).status_code == 500

    def test_coin_change_with_too_big_coin(self):
        assert post_form('2147483648', 3).status_code == 500

    def test_coin_change_with_negative_amount(self):
        assert post_form('1 2 3', -1).status_code == 500

    def test_coin_change_with_too_big_amount(self):
        assert post_form('1 2 3', 10 ** 4 + 1).status_code == 500

    def test_coin_change_with_minimum_coins_length_possible(self):
        assert post_form('1', 12).text == '12'

    def test_coin_change_with_maximum_coins_length_possible(self):
        assert post_form('1 2 3 4 5 6 7 8 9 10 11 12', 12).text == "1"

    def test_coin_change_with_maximum_coin_possible(self):
        assert post_form(str(2 ** 31 - 1), str(5)).text == "-1"

    def test_coin_change_with_minimum_coin_possible(self):
        assert post_form('1 2 5', 3).text == "2"

    def test_coin_change_with_maximum_amount_possible(self):
        assert post_form('1', str(10 ** 4)).text == "10000"

    def test_coin_change_with_string_amount_input(self):
        assert post_form('1 2 3', 'abyrvalg').status_code == 500

    def test_coin_change_with_string_array_input(self):
        assert post_form('odin dva tri', 5).status_code == 500
