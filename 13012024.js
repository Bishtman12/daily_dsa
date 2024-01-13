//! Problem Link : https://www.geeksforgeeks.org/problems/insertion-sort-for-singly-linked-list/1

//User function Template for javascript

/**
 * @param {Node} node
 * @return {Node} node
*/


/*
class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

let head;
This is method only submission.
You only need to complete the below method.
*/

class Solution {
    insertionSort(node) {
        if (!head || !head.next) {
            return head
        }
        // making dummy the head of the list
        let dummy = new Node(-1);
        dummy.next = head;

        let current = head

        while (current.next) {
            // if next element is smaller then find the insert index
            if (current.data > current.next.data) {
                //store the node
                let temp = current.next;
                //remove the node from list
                current.next = current.next.next
                //
                let i = dummy;
                while (i.next && (i.next.data < temp.data)) {
                    i = i.next
                }
                temp.next = i.next;
                i.next = temp
            }
            else {
                current = current.next
            }

        }
        return dummy.next
    }
}