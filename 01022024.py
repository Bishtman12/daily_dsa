#Problem Link https://www.geeksforgeeks.org/problems/pangram-checking-1587115620/1

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        return len(set([i.lower() for i in s if ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90]))==26
