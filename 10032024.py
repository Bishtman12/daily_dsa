#Problem Link https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1 

class Solution:

	
	def removeDuplicates(self,str):
	    
	    hmap = {} 
	    ans = ""
	    for i in str:
	        if i in hmap:
	            continue
	        else:
	            ans += i 
	            hmap[i] = 1 
	    return ans