class Node {
    constructor(x) {
        this.data = x;
        this.next = null;
    }
    decimalValue(head){
        let new_head = this.reverseLinkedList(head);
        const MOD = 10**9+7;
        let answer = 0;
        let i = 0;
        
        while (new_head) {
            if (i == 0 && new_head.data == 0){
                new_head = new_head.next
                i += 1
                continue
            }
            console.log(new_head.data)
            let num = 1;
            new_head.data == 1 ? num = 2 : num  = 1;

            answer = answer + num ** i
            new_head = new_head.next
            i += 1
        }
        console.log(answer)
        return answer%MOD
      
  }

    reverseLinkedList(head) {
        let temp = null;
        let prev = null;
        while (head) {
            temp = head.next;
            head.next = prev;
            prev = head;
            head = temp

        }
        return prev
    }

    printList(head){
        let new_head = this.reverseLinkedList(head);
        console.log(new_head)
        while (new_head){
            console.log(new_head.data);
            new_head = new_head.next
        }
    }
}

const A = new Node("0");
const B = new Node("1");
const C = new Node("1");
const D = new Node("0");
A.next = B;

B.next = C

// C.next = D

// A.printList(A); // Invoking the printList function
A.decimalValue(A)
console.log(2**0)
