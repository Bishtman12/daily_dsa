// ! Problem Link : https://www.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1

class Queue {
    constructor() {
        this.arr = [];
        this.front = 0;
    }

    push(a) {
        this.arr.push(a);
    }

    pop() {
        if (this.arr.length != this.front) {
            let x = this.arr[this.front];
            this.front++;
            return x;
        }
        else
            return -1;
    }

    front_ele() {
        return this.arr[this.front];
    }

    empty() {
        if (this.arr.length != this.front)
            return false;
        else
            return true;
    }
}

class Solution {
    // Function to reverse first k elements of a queue.
    modifyQueue(q, k) {
        const arr = q.arr;
        k -= 1
        let i = 0;

        while (i < k) {
            const temp = arr[i];
            arr[i] = arr[k];
            arr[k] = temp;
            i += 1
            k -= 1
        }
        q.arr = arr;
        return q
    }
}