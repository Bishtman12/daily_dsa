# !Problem Link : https://www.geeksforgeeks.org/problems/grinding-geek/1


from typing import List


class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        
        def helper(n,t):
            if dp[n][t]!= -1:
                return dp[n][t]
            elif n == 1:
                if t>= cost[n-1]:
                    dp[n][t] = 1
                else:
                    dp[n][t] = 0
                return dp[n][t]
            else:
                ans = helper(n-1,t)
                if t>=cost[n-1]:
                    ans = max(ans,1+helper(n-1,t-cost[n-1]+int(cost[n-1]*0.9)))
                dp[n][t] = ans
                return ans
        
        dp=[[-1]*(total+1) for _ in range(n+1)]
        cost=cost[::-1]
        return helper(n,total)