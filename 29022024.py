# Problem Link : https://www.geeksforgeeks.org/problems/sum-of-bit-differences2937/1

class Solution:

	
	def sumBitDifferences(self,arr, n):
	    ans = 0 
	    
	    for i in range(32):
	        setBits = 0 
	        unsetBits = 0 
	        for num in arr:
	            if num & (1 << i):
	                setBits += 1 
	            else:
	                unsetBits += 1 
	        ans += setBits * unsetBits * 2 
	    return ans