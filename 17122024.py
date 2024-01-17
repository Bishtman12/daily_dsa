# ! Problem Link : https://www.geeksforgeeks.org/problems/all-unique-permutations-of-an-array/1
def uniquePerms(self, arr, n):
    # code here 
    def helper(index):
        if index == n:
            result.append(arr[:])
            return
        hmap = set()
        for i in range(index,n):
            if arr[i] not in hmap:
                hmap.add(arr[i])
                arr[index] , arr[i] = arr[i],arr[index]
                helper(index + 1)
                arr[index],arr[i] = arr[i], arr[index]
    result = []
    helper(0)
    result.sort()
    return result