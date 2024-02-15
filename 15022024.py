#Problem Link : https://www.geeksforgeeks.org/problems/castle-run3644/1
class Solution:
	def isPossible(self, paths):
	    
	    for i in paths:
	        sum = 0
	        for j in i:
	            sum += j
	        if sum % 2 != 0:
	            return 0
	    return 1