# Problem Link : https://www.geeksforgeeks.org/problems/sum-of-leaf-nodes-in-bst/1

class Solution:
    def sumOfLeafNodes(self, root):
        
        if not root:
            return 0
        if not (root.left or root.right):
            return root.data
        a = self.sumOfLeafNodes(root.left);
        b = self.sumOfLeafNodes(root.right);
        return a+b