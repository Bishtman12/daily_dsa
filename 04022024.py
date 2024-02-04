#Problem Link :https://www.geeksforgeeks.org/problems/subtraction-in-linked-list/1

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        str1 = ""
        while (l1):
            str1 += str(l1.data)
            l1 = l1.next
        
        str2 = ""
        
        while (l2):
            str2 += str(l2.data)
            l2 = l2.next
            
        str1 = int(str1);
        str2 = int(str2);
        ans = str(max(str1,str2) - min(str1,str2));
        
        first = Node(ans[0])
        head = first
        for i in ans[1:]:
            temp = Node(i);
            head.next = temp;
            head = temp;
        return first