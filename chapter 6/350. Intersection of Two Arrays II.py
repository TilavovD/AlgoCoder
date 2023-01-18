# https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/880502779/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = dict()
        out = list()
        for i in nums1:
            nums[i] = 1 if i  not in nums else nums[i] + 1
        for i in nums2:
            if i in nums and nums[i] > 0:
                out.append(i)
                nums[i] -= 1
        return out
