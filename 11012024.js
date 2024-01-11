// ! Problem Link : https://www.geeksforgeeks.org/problems/remove-k-digits/1

class Solution {
    removeKdigits(s, k) {

        const stack = [];
        for (const element of s) {
            while (stack.length && stack[stack.length - 1] > element && k > 0) {
                stack.pop()
                k -= 1
            }

            if (stack.length || element != "0") {
                stack.push(element)
            }
        }
        while (stack.length && k > 0) {
            stack.pop()
            k -= 1
        }
        return (stack.length ? stack.join('') : '0')
    }
}