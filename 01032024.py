#Problem Link https://www.geeksforgeeks.org/problems/peak-element/1

# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
            
        low, high = 0, n-1;
        
        if n==1:
            return 0 
            
            
        while low < high:
            
            mid = low + (high -low)//2
            
            if arr[mid]>arr[mid+1]:
                high = mid
            else:
                low = mid+1
        
        return low
        