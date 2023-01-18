# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        nums1 = set(nums1)
        for i in set(nums2):
            if i in nums1:
                out.append(i)
        return out
