# Problem Link https://www.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1

class Solution:
    def firstElementKTime(self, n, k, a):
        
        hmap = {}
        
        for i in a:
            if i in hmap:
                if hmap[i]+1 == k:
                    return i
                else:
                    hmap[i] = hmap[i]+1
            else:
                hmap[i] = 1
                    
        return -1