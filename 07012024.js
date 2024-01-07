// ! problem link : https://www.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1?page=2&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions
class Solution {
    findOnce(arr, n) {
        let low = 0;
        let high = n - 1;

        while (low < high) {
            let mid = Math.floor((low + high) / 2);

            // If mid is even and element next to mid is same as mid, then output element lies on right side, else on left side
            if (mid % 2 === 0) {
                if (arr[mid] === arr[mid + 1]) {
                    low = mid + 2;
                } else {
                    high = mid;
                }
            } else { // If mid is odd
                if (arr[mid] === arr[mid - 1]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        return arr[low];
    }
}