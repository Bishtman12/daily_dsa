#User function Template for python3
# Problem Link : https://www.geeksforgeeks.org/problems/flatten-bst-to-sorted-list--111950/1
import sys
sys.setrecursionlimit(10**5)
    

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def flattenBST(self, root):
        
        def inorder(root):
            res=[]
            if root.left:
                res=res+inorder(root.left)
            res.append(root.data)
            if root.right:
                res=res+inorder(root.right)
            return res
        
        arr = inorder(root)
        head = Node(arr[0])
        sudo_head = head 
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            sudo_head.right = temp 
            sudo_head = temp 
        return head
        # code here
