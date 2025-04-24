from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))  # number of distinct elements in the whole array
        n = len(nums)
        result = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == total_unique:
                    result += 1

        return result

        