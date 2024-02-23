#Problem Link https://www.geeksforgeeks.org/problems/buy-and-sell-a-share-at-most-twice/1

from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        arr=[0]*(n)
        maxi = price[-1]
        ans = 0 
        for i in range(n-1, -1 , -1):
            if price[i] >  maxi : 
                maxi = price[i]
                
            else : 
                ans= max(ans,maxi- price[i])
                arr[i]= ans 
              
        mini = price[0]
        ansi = 0 
        num=[0]*n
        for i in range(n):
            if price[i] < mini : 
                mini = price[i]
            else : 
                ansi = max(price[i]- mini, ansi )
                num[i]= ansi
            
        #print(arr, num)
        fans = max(num[-1], arr[0])
        for i in range(n-1):
            fans = max(fans , num[i]+ arr[i+1])
            
        return  fans