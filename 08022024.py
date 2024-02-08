#Problem Link : https://www.geeksforgeeks.org/problems/leaf-at-same-level/1

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        if not root:
            return 0
        l = self.check(root.left)
        
        if l is False:
            return False
        r = self.check(root.right)
        if r is False:
            return False
        if l==r:
            return 1+l
        elif l == 0 or r==0:
            return 1+l+r
        return False