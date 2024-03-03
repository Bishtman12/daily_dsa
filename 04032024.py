# Problem Link : https://www.geeksforgeeks.org/problems/need-some-change/1


class Solution:
	def swapElements(self, arr, n):
	    
	    for i in range(n-2):
	        arr[i],arr[i+2] = arr[i+2],arr[i]
	    return arr
	    