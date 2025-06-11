class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        idx = [[] for _ in range(5)]
        for i, c in enumerate(s): idx[int(c)].append(i)
        idx = [q + [len(s)] for q in idx if q]
        def sol(q1, q2):
            que, prev, i, j, best, curr = [deque() for _ in range(4)], [inf]*4, 0, 0, -inf, -1
            que[0].append((max(q1[0], q2[0], k - 1), 0))
            while q1[i] != q2[j]:
                if q1[i] < q2[j]: curr = max(curr, q1[i]); i += 1
                else: curr = max(curr, q2[j]); j += 1
                r = min(q1[i], q2[j]) - 1
                p, pp = (i & 1) | ((j & 1) << 1), (i & 1) ^ 1 | ((j & 1) << 1)
                while que[pp] and que[pp][0][0] <= r: _, prev[pp] = que[pp].popleft()
                best = max(best, i - j - prev[pp])
                v = i - j
                if v < prev[p] and (not que[p] or v < que[p][-1][1]):
                    que[p].append((max(curr + k, q1[i], q2[j]), v))
            return best
        return max(sol(a, b) for a, b in permutations(idx, 2))