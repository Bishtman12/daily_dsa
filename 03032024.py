#Problem Link https://www.geeksforgeeks.org/problems/largest-number-formed-from-an-array1117/1

class Solution:

	def printLargest(self, n, arr):
	    
	    arr = sorted(arr,key = lambda x:str(x)*10 , reverse = True)
	    ans = ""
	    
	    for i in arr:
	        ans += i 
	    return ans