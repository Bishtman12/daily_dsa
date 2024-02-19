#problem Link : https://www.geeksforgeeks.org/problems/game-with-string4100/1
from collections import defaultdict 
import heapq
class Solution:
    def minValue(self, s, k):
        # code here
        n = len(s)
        mp = defaultdict(int)
        
        for char in s:
            mp[char] += 1
        
        pq = [-count for count in mp.values()]
        heapq.heapify(pq)
        
        while k > 0:
            x = heapq.heappop(pq) + 1
            heapq.heappush(pq, x)
            k -= 1
        
        total = sum(count ** 2 for count in pq)
        
        return total
