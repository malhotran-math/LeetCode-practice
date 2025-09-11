# A naive code, with complexity O((m+n)log(m+n))
import statistics 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        List = nums1 + nums2 
        List.sort() 
        med = statistics.median(List)
        return med 
