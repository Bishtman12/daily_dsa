#Problem Link : https://www.geeksforgeeks.org/problems/power-set4302/1

class Solution:
	def AllPossibleStrings(self, s):
	    res = []
		
		def solve(st, i):
		    if i == len(s):
		        return
		    
		    res.append(st+s[i])
		    
		    solve(st+s[i], i+1)
		    solve(st, i+1)
	    
	    solve("", 0)
	    return sorted(res)