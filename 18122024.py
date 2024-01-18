#! Problem Link : https://www.geeksforgeeks.org/problems/water-the-plants--170646/1

def min_sprinklers(self, gallery, n):
    limit = []
    for i in range(n):
        if gallery[i] != -1:
            limit.append([max(0, i - gallery[i]), min(n-1, i + gallery[i])])
    

    limit.sort()

    sprinklers = 0
    i = 0
    start = 0
    while start < n:
        max_range = -1
        while i < len(limit) and limit[i][0] <= start:
            max_range = max(max_range, limit[i][1])
            i += 1


        if max_range < start:
            return -1

        sprinklers += 1
        start = max_range + 1
    return sprinklers