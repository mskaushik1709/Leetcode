class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def get_distances(start):
            n = len(edges)
            dist = [-1] * n
            visited = [False] * n
            curr = start
            d = 0
            while curr != -1 and not visited[curr]:
                dist[curr] = d
                visited[curr] = True
                curr = edges[curr]
                d += 1
            return dist
        
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        answer = -1
        min_max_dist = float('inf')
        
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_max_dist:
                    min_max_dist = max_dist
                    answer = i
                elif max_dist == min_max_dist and i < answer:
                    answer = i
                    
        return answer
