#Problem Link : https://www.geeksforgeeks.org/problems/check-if-a-number-is-divisible-by-83957/1
class Solution:
    def DivisibleByEight(self,s):
        # just have to check the last 3 digit of a number 
        s = int(s[-3:])
        
        if (s%8 == 0):
            return 1
        return -1