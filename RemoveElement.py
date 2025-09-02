class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
