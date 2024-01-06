// ! Problem Link : https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?page=1&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions
// ! arr = [7,2,0, 4] ans = 10
class Solution {
    // Function to find the trapped water between the blocks.
    trappingWater(arr, n) {
        const storage = [];
        let high = arr[0];
        for (const wall of arr) {
            //store the highest wall of one side; 
            if (wall > high) {
                high = wall;
            }
            storage.push(high)
        }
        let answer = 0;
        high = arr[n - 1]
        for (let i = n - 1; i > -1; i--) {
            const wall = arr[i];
            if (wall > high) {
                high = wall
            }
            if (storage[i] > high) {
                storage[i] = high
            }
        }

        for (let i = 0; i < n; i++) {
            answer += (storage[i] - arr[i])
        }
        return answer

    }
}