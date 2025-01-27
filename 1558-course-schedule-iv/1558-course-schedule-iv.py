class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        mp = {}
        res = []

        def dfs(crs):
            if crs not in mp:
                mp[crs] = set()
                for nei in graph[crs]:
                    mp[crs] |= dfs(nei)
                mp[crs].add(crs)
            return mp[crs]
        for a,b in prerequisites:
            graph[b].append(a)

        for course in range(numCourses):
            dfs(course)
            
        for u,v in queries:
            res.append(u in mp[v])

        print(res)

        return res