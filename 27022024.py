#Problem Link : https://www.geeksforgeeks.org/problems/play-with-or5515/1
class Solution:
    def game_with_number (self, arr,  n) : 
        
        for i in range(n-1):
            arr[i] = arr[i] | arr[i+1]
        return arr