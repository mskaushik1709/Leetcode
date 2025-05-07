import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            t, x, y = heapq.heappop(heap)
            if x == n - 1 and y == m - 1:
                return t
            if t > dist[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    new_time = max(t, moveTime[nx][ny]) + 1
                    if new_time < dist[nx][ny]:
                        dist[nx][ny] = new_time
                        heapq.heappush(heap, (new_time, nx, ny))
        return -1
