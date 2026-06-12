class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # Map each course to its prerequisites
        # preMap = {i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)

        # visiting = set()

        # def dfs(crs):
        #     if crs in visiting:
        #         return False
        #     if preMap[crs] == []:
        #         return True
            
        #     visiting.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visiting.remove(crs)
        #     preMap[crs] = []
        #     return True
        
        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True

        # Kahn algo
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        print( indegree, adj)
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses
            
        