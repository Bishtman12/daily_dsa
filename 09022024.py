# Problem Link https://www.geeksforgeeks.org/problems/children-sum-parent/
class Solution:
    def isSumProperty(self, root):
        # code here
        if root:
            if not root.left and not root.right:
                return 1
            s = root.left.data if root.left else 0
            s+= root.right.data if root.right else 0
            
            if s!=root.data:
                return 0
            if self.isSumProperty(root.left) and self.isSumProperty(root.right):
                return 1
            else:
                return 0
        return 1