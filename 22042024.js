// ! Problem Link : https://www.geeksforgeeks.org/problems/paths-from-root-with-a-specified-sum/1

class Node {
    constructor(val) {
        this.key = val;
        this.left = null;
        this.right = null;
    }

    inOrderTraverse(root) {

        if (!root) return
        this.inOrderTraverse(root.left)
        console.log(root.key)
        this.inOrderTraverse(root.right)
    }

    preOrderTraverse(root) {
        if (!root) return
        console.log(root.key)
        this.preOrderTraverse(root.left)
        this.preOrderTraverse(root.right)
    }

    postOrderTraverse(root) {
        if (!root) return
        this.postOrderTraverse(root.left)
        this.postOrderTraverse(root.right)
        console.log(root.key)
    }

    printPaths(root, sum) {
        const result = []
        const path = []
        function helper(root,cur_sum,result,path){
            if (!root) return
            
            path.push(root.key);
            
            if((cur_sum + root.key) == sum){
                result.push(path.slice())
            }
            helper(root.left, cur_sum + root.key , result , path)
            helper(root.right, cur_sum + root.key , result , path)
            path.pop()
        }
        helper(root,0,result,path);
        return result
    }
}


/*
      1
   2     3
  4 5   
  inorder -> 4 2 5 1 3 ( left root right )
  pre-order -> 1 2 4 5 3 (root left right)
  post-order -> 4 5 2 3 1 (left right root)
*/

const root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);
root.left.right = new Node(5);

console.log("Pre Order traversal of binary tree is ");
root.inOrderTraverse(root);

console.log("Pre Order traversal of binary tree is ");
root.preOrderTraverse(root);

console.log("Post Order traversal of binary tree is ");
root.postOrderTraverse(root);
