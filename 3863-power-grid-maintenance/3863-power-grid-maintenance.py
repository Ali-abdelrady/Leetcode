class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 1) Build the graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Make sure every station (1..c) exists in the graph, even if isolated
        for i in range(1, c + 1):
            graph[i]  # ensures node is present in the dict

        # 2) Initialize online stations
        online_stations = set(range(1, c + 1))

        # 3) Find connected components (DFS)
        visited = set()
        components = []
        component_id = {}

        def dfs(node, comp_index):
            stack = [node]
            group = []
            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                component_id[cur] = comp_index
                group.append(cur)
                for nei in graph[cur]:
                    if nei not in visited:
                        stack.append(nei)
            return sorted(group)

        comp_index = 0
        for node in graph:
            if node not in visited:
                group = dfs(node, comp_index)
                components.append(group)
                comp_index += 1

        print(components)
        # 4) Process queries
        res = []
        for op, station in queries:
            if op == 1:
                if station in online_stations:
                    res.append(station)
                else:
                    comp_idx = component_id.get(station)
                    if comp_idx is None:
                        res.append(-1)
                        continue

                    group = components[comp_idx]
                    # Remove all offline stations from the front
                    while group and group[0] not in online_stations:
                        group.pop(0)

                    res.append(group[0] if group else -1)
            elif op == 2:
                online_stations.discard(station)

        return res
