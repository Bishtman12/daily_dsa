#Problem Link : https://www.geeksforgeeks.org/problems/maximum-sum-problem2211/1

class Solution:
    def maxSum(self, n): 
        s=n//3 + n//2 + n//4
        if s <=n:
            return n
        else:
            return max(n//3,self.maxSum(n//3))+max(n//2,self.maxSum(n//2))+max(n//4,self.maxSum(n//4))