# https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        out = []

        for i in range(len(nums)):
            if nums[i] == target:
                out.append(i)
            elif nums[i] > target:
                break
        return out
