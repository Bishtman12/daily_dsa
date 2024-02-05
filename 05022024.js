// Problem Link : https://www.geeksforgeeks.org/problems/sorted-insert-for-circular-linked-list/1

class Solution {
    
    sortedInsert(head, data)
    {
        const insert_node = new Node(data);
        const store_head = head;
        let prev = new Node(null);
        
        if(head === null){
            insert_node.next = insert_node;
            return insert_node
        }
        // first element of the list
        if(data<= head.data){
            insert_node.next = head;
            while (head.next != store_head){
                head = head.next
            }
            head.next = insert_node;
            return insert_node
        }
        
        while (head.next != store_head && head.next.data <= data) {
            head = head.next
        }
        insert_node.next = head.next;
        head.next = insert_node;
        return store_head
    }
    
}
