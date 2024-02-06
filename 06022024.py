# Problem Link : https://www.geeksforgeeks.org/problems/node-at-distance/1
class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        
        def helper(root,level,k,ans,hmap):
            if root == None:
                return 
            ans.append(root)
            if root.left == None and root.right == None:
                index = level - k
                if index >= 0:
                    hmap.add(ans[index])
                return
            helper(root.left,level+1,k,ans.copy(),hmap)
            helper(root.right,level+1,k,ans.copy(),hmap)

        
        hmap = set();
        ans = []
        helper(root,0,k,ans.copy(),hmap)
        return len(hmap)