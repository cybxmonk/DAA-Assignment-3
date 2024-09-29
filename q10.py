class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                if dp[j - coin] != float('inf'):
                    dp[j] = min(dp[j], dp[j - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]

solution = Solution()
coins = [1, 2, 5]
amount = 11
print(solution.coinChange(coins, amount))
