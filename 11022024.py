# Problem Link : https://www.geeksforgeeks.org/problems/recamans-sequence4856/1
class Solution:
    def recamanSequence(self, n):
        
        result = [0];
        hmap = {0:1}
        for i in range(1,n):
            
            term1 = result[i-1] - i;
            term2 = result[i-1] + i
            
            if (term1>0 and term1 not in hmap):
                result.append(term1)
                hmap[term1] = 1
            else:
                result.append(term2)
                hmap[term2] = 1
        return result