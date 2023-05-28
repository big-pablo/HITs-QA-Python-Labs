from typing import List


class FixedSolution:
    def coinChange(self, old_coins: List[int], old_amount: int) -> int:
        coins = self.validateIntCoins(old_coins)
        amount = self.validateIntAmount(old_amount)
        if amount < 0 or amount > 10 ** 4:
            raise ValueError
        if len(coins) > 12 or len(coins) < 1:
            raise ValueError
        for coin in coins:
            if coin > 2 ** 31 - 1 or coin < 1:
                raise ValueError
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

    def validateIntCoins(self, coins):
        new_coins = []
        try:
            for coin in coins:
                if type(coin) == float:
                    raise ValueError
                new_coins.append(int(coin))
            return new_coins
        except:
            raise ValueError

    def validateIntAmount(self, amount):
        try:
            if type(amount) == float:
                raise ValueError
            return int(amount)
        except:
            raise ValueError
