
class Solution:
    def vP(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)] 
        visited = [False for _ in range(n)]
        for e in edges:
            v1, v2 = e[0], e[1]
            adj[v1].append(v2)
            adj[v2].append(v1)

        if source == destination: 
            return True

        if len(adj) == 0 or len(edges) == 0:
            return False
        if adj[destination] == []:
            return False

        q = [destination]
        visited[destination] = True
        while len(q):
            v = q.pop(0)
            for vnext in adj[v]:
            
                if vnext == source: 
                    return True

                if visited[vnext] == False: 
                    q.append(vnext)
                    visited[vnext] = True
                    
        return False
        
# Another example:
edges = [[0, 1], [1, 2], [2, 3]]  # Example graph edges
n = 4  # Number of nodes
source = 3  # Starting node
destination = 0  # Target node

solution = Solution()
result = solution.vP(n, edges, source, destination)
print(result)  # Expected output: False