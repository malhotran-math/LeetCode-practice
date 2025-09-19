class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for pos, val in enumerate(nums):
            if pos > reach: 
                return False
            reach = max(reach, pos + val)
        return True

#This is a greedy algorithm approach. It does not care if your jumps are optimal, but the algorithm is efficient enough, running in O(n)
#time where n = len(nums). 
