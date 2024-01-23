# Problem LInk https://www.geeksforgeeks.org/problems/course-schedule/1
def findOrder(self, n, m, prerequisites):
        graph = [[] for i in range(n)]
        for dest,src in prerequisites:
            graph[src].append(dest)
        indegree = [0 for i in range(n)]
        for i in graph:
            for j in i:
                indegree[j] += 1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        if len(q) == 0:
            return []
        ans = []
        while(q):
            size = len(q)
            while(size):
                ele = q.pop()
                ans.append(ele)
                for nbrs in graph[ele]:
                    indegree[nbrs] -= 1
                    if indegree[nbrs] == 0:
                        q.append(nbrs)
                size-=1
        if len(ans) == n:
            return ans
        else:
            return []