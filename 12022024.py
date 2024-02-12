# Problem Link : https://www.geeksforgeeks.org/problems/recursive-sequence1611/1
class Solution:
    def sequence(self, n):
        MOD = 10**9+7
        if n == 1:
            return 1 
        temp = 1
        ans = 1
        x = 1
        for i in range(2,n+1):
            for j in range(0,i):
                temp += 1
                x = x*temp
            ans += x
            x = 1
        return ans%MOD
                