# ! Problem Link : https://www.geeksforgeeks.org/problems/coin-change2448/1?page=2&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

class Solution:
    def count(self, coins, N, Sum):
        dp=[0]*(Sum+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin,Sum+1):
                dp[j]+=dp[j-coin]
        return dp[Sum]