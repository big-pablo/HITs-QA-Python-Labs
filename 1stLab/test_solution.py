from unittest import TestCase
from solution import Solution

class TestSolution(TestCase):
    def test_coin_change_with_reachable_sum(self):
        sut = Solution()
        assert sut.coinChange([85,89,7], 431) == 17
    def test_coin_change_with_impossible_coins_combination(self):
        sut = Solution()
        assert sut.coinChange([2,5,10,12],3) == -1
    def test_coin_change_with_zero_amount(self):
        sut = Solution()
        assert sut.coinChange([1,12,5], 0) == 0
    def test_coin_change_with_no_coins_input(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.coinChange([], 12)
    def test_coin_change_with_too_much_coins(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.coinChange([x for x in range(1,14)], 1)
    def test_coin_change_with_negative_coins(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.coinChange([-1, 4], 3)
    def test_coin_change_with_too_big_coin(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.coinChange([(2**31)], 3)
    def test_coin_change_with_negative_amount(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.coinChange([1, 2, 3], -1)
    def test_coin_change_with_too_big_amount(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.coinChange([1,2,3], 10**4+1)
    def test_coin_change_with_minimum_coins_amount_possible(self):
        sut = Solution()
        assert sut.coinChange([1], 12) == 12
    def test_coin_change_with_maximum_coins_amount_possible(self):
        sut = Solution()
        assert sut.coinChange([x for x in range(1,12)],12) == 2
    def test_coin_change_with_maximum_coin_possible(self):
        sut = Solution()
        assert  sut.coinChange([(2**31)-1, 10], 10) == 1
    def test_coin_change_with_minimum_coin_possible(self):
        sut = Solution()
        assert sut.coinChange([1,2,5], 3) == 2
    def test_coin_change_with_maximum_amount_possible(self):
        sut = Solution()
        assert sut.coinChange([1], 10**4) == 10000