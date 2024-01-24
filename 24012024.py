#Problem Link : https://www.geeksforgeeks.org/problems/is-it-a-tree/1

class Solution:
    def dfs(self,adj,s):
        n=len(adj)
        visited=[False]*n
        stack=[(s,-1)]
        visited[s]=True
        while stack:
            u,parent=stack.pop()
            for v in adj[u]:
                if visited[v]==False:
                    stack.append((v,u))
                    visited[v]=True
                elif v!=parent:
                    return 0
        if False in visited:
            return 0
        return 1

    def isTree(self, n, m, edges):
        adj=[[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        return self.dfs(adj,0)