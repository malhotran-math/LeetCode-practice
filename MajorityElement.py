class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elems = set(nums)
        for elem in elems: 
            if nums.count(elem)>len(nums)/2:
                majority_elem = elem
                break
        return majority_elem
