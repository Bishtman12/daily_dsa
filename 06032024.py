# Problem Link : https://www.geeksforgeeks.org/problems/search-pattern-rabin-karp-algorithm--141631/1

class Solution:
    def search(self, pattern, text):
        text_length = len(text)
        pattern_length = len(pattern)
        
        if text_length < pattern_length:
            return -1 
        ans = []
        for i in range(text_length):
            if text[i:i+pattern_length] == pattern:
                ans.append(1+i)
        return ans