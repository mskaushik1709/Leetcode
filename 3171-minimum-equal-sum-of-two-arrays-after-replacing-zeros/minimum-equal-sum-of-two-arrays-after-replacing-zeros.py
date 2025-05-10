class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        z1, z2 = nums1.count(0), nums2.count(0)

        if s1 == s2:
            if z1 == 0 and z2 == 0:
                return s1

        base1, base2 = s1 + z1, s2 + z2

        

        if base1 > base2:
            if z2 == 0:
                return -1
            else:
                return base1
        else:
            if z1 == 0:
                return -1
            else:
                return base2