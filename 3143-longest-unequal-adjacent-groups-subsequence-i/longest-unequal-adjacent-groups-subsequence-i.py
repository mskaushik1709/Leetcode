from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        n = len(words)
        dp = [1] * n         # dp[i] = length of longest alternating subsequence ending at i
        prev = [-1] * n      # prev[i] = previous index in the optimal subsequence ending at i

        max_len = 1
        end_index = 0

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                end_index = i

        # Reconstruct result from end_index
        res = []
        while end_index != -1:
            res.append(words[end_index])
            end_index = prev[end_index]

        return res[::-1]  # reverse to return in original order
