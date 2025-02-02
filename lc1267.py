class Solution:

    # 1267. Count Servers that Communicate
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        servers = set()
        
        for r in range(m):
            connected = {(r,c) for c in range(n) if grid[r][c] != 0}
            if len(connected) > 1:
                servers.update(connected)

        for c in range(n):
            connected = {(r,c) for r in range(m) if grid[r][c] != 0}
            if len(connected) > 1:
                servers.update(connected)

        return len(servers)