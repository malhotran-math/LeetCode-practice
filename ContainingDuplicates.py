#This is a neat dictionary approach, taking O(n) time. 


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = nums.count(k)
        last_seen = {}  # stores last index of each number
        for i, val in enumerate(nums):
            if val in last_seen and i - last_seen[val] <= k:
                return True
            last_seen[val] = i
        return False


