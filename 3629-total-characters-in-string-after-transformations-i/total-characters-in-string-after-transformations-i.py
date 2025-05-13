class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        MOD = 10**9 + 7
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1

        for _ in range(t):
            next_counts = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    next_counts[0] = (next_counts[0] + counts[25]) % MOD
                    next_counts[1] = (next_counts[1] + counts[25]) % MOD
                else:
                    next_counts[i + 1] = (next_counts[i + 1] + counts[i]) % MOD
            counts = next_counts
        
        return sum(counts) % MOD
