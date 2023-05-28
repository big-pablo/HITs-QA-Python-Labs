from unittest import TestCase
from solutions.solution import Solution


class TestSolution(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.SUT = Solution()

    def test_coin_change_with_reachable_sum(self):
        self.assertEqual(self.SUT.coinChange([85, 89, 7], 431), 17)

    def test_coin_change_with_impossible_coins_combination(self):
        self.assertEqual(self.SUT.coinChange([2, 5, 10, 12], 3), -1)

    def test_coin_change_with_minimum_amount_possible(self):
        self.assertEqual(self.SUT.coinChange([1, 12, 5], 0), 0)

    def test_coin_change_with_no_coins_input(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([], 12)

    def test_coin_change_with_too_much_coins(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([x for x in range(1, 14)], 1)

    def test_coin_change_with_negative_coin(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([-1, 4], 3)

    def test_coin_change_with_too_big_coin(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([(2 ** 31)], 3)

    def test_coin_change_with_negative_amount(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([1, 2, 3], -1)

    def test_coin_change_with_too_big_amount(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([1, 2, 3], 10 ** 4 + 1)

    def test_coin_change_with_minimum_coins_length_possible(self):
        self.assertEqual(self.SUT.coinChange([1], 12), 12)

    def test_coin_change_with_maximum_coins_length_possible(self):
        self.assertEqual(self.SUT.coinChange([x for x in range(1, 13)], 12), 1)

    def test_coin_change_with_maximum_coin_possible(self):
        self.assertEqual(self.SUT.coinChange([(2 ** 31) - 1, 10], 10), 1)

    def test_coin_change_with_minimum_coin_possible(self):
        self.assertEqual(self.SUT.coinChange([1, 2, 5], 3), 2)

    def test_coin_change_with_maximum_amount_possible(self):
        self.assertEqual(self.SUT.coinChange([1], 10 ** 4), 10000)

    def test_coin_change_with_num_as_string_array_input(self):
        self.assertEqual(self.SUT.coinChange(["1", "2", "3"], 5), 2)

    def test_coin_change_with_num_as_string_amount_input(self):
        self.assertEqual(self.SUT.coinChange([1, 2, 3], '5'), 2)

    def test_coin_change_with_string_amount_input(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([1, 2, 3], 'abyrvalg')

    def test_coin_change_with_string_array_input(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange(["odin", "dva", "tri"], 5)

    def test_coin_change_with_float_numbers_in_coins(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([1.2, 5.5,], 11)

    def test_coin_change_with_float_number_in_amount(self):
        with self.assertRaises(ValueError):
            self.SUT.coinChange([6,2,5], 12.5)