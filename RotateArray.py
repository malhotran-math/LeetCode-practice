import numpy as np
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numscopy = tuple(nums) #important, you don't want to alter
        #the copy of nums
        for i in np.arange(k,len(nums)):
            nums[i] = numscopy[i-k]
        for i in range(k):
            nums[i] = numscopy[len(nums)-k+i]
