//! Problem Link : https://www.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1

class Solution {
    longSubarrWthSumDivByK(arr, n, k) {

        const hmap = { 0: -1 }
        let sum = 0;
        let max_length = 0;

        for (let i = 0; i < n; i++) {
            sum += arr[i];
            const remainder = ((sum % k) + k) % k;
            if (remainder in hmap) max_length = Math.max(max_length, i - hmap[remainder]);
            else hmap[remainder] = i
        }
        return max_length
    }
}