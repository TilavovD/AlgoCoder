class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left<right:
            mid = (left +right)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left] if letters[left]>target else letters[0]
