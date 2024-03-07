#Problem Link https://www.geeksforgeeks.org/problems/check-frequencies4211/1 

#User function Template for python3
class Solution:
    def sameFreq(self, s):
        
        hmap = {}
        
        for i in s:
            if i in hmap:
                hmap[i] = hmap[i] + 1
            else:
                hmap[i] = 1
                
        mis_match_count = 0
        prev = None
        
        for a in hmap.values():
            if prev is None:
                prev = a
                continue
            if a != prev:
                mis_match_count += abs(prev-a)
        return 0 if mis_match_count >= 2 else 1