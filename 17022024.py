#Problem Link https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1
class Solution:
    def isMaxHeap(self,arr,n):
        
        for i in range(1,n):
            x = (i+1)//2
            if arr[x-1] < arr[i]:
                return False
        return True