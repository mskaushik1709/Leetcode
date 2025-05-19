from typing import List
class Solution:
    def triangleType(self, nums: List[int]) -> str:

        a, b, c = sorted(nums)  # Sort the sides to simplify triangle inequality check

        # Check if it can form a triangle
        if a + b <= c:
            return "none"

        # All sides equal → Equilateral
        if a == b == c:
            return "equilateral"

        # Two sides equal → Isosceles
        if a == b or b == c or a == c:
            return "isosceles"

        # All sides different → Scalene
        return "scalene"
