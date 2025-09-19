class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):  
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps


#this runs in O(n) time. The algorithm idea is simple. You keep track of what the "current end" of your jump range is, and the farthest reach
# you have had so far. The moment you reach your current end, you jump, and your new end is updated as the farthest reach. 
