# Problem Link https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        arr.sort(key=lambda x:x.value/x.weight, reverse=True)
        res = 0
        for i in range(n):
            if W>=arr[i].weight:
                res += arr[i].value
                W -= arr[i].weight
            elif W>0:
                res += (arr[i].value/arr[i].weight)*W
                W -= arr[i].weight
        return res