class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for pos, val in enumerate(nums):
            if pos > reach: 
                return False
            reach = max(reach, pos + val)
        return True
