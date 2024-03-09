#Problem Link https://www.geeksforgeeks.org/problems/find-the-n-th-character5925/1


class Solution:
    def nthCharacter(self, s, r, n):
        
        # cut short the temp
        def helper(temp,n):
            new_temp = ""
            i = 0
            while True:
                if len(new_temp) >= (n+1):
                    break
                else:
                    if temp[i] == "0":
                        new_temp += "01"
                    else:
                        new_temp += "10"
                    i += 1 
            return new_temp
        
        new_string = s;
        while r>0:
            new_string = helper(new_string,n)
            r -= 1 
        return new_string[n]