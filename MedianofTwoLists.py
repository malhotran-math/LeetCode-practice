import statistics 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     List = nums1 + nums2 
    #     List.sort() 
    #     med = statistics.median(List)
    #     return med 
    #The obove is a naive O((m+n)log(m+n)) code. faster one below. 

        #The following is O(log(m+n)).

        def get_kth_element(k):
            i = j = 0
            while True:
                if i == len(nums1):
                    return nums2[j + k - 1]
                if j == len(nums2):
                    return nums1[i + k - 1]
                if k == 1:
                    return min(nums1[i], nums2[j])
            
                # Compare k//2-th elements in remaining parts
                new_i = min(i + k // 2 - 1, len(nums1) - 1)
                new_j = min(j + k // 2 - 1, len(nums2) - 1)
            
                if nums1[new_i] <= nums2[new_j]:
                    k -= new_i - i + 1
                    i = new_i + 1
                else:
                    k -= new_j - j + 1
                    j = new_j + 1
        m, n = len(nums1), len(nums2)
        total = m + n
        if total % 2 == 1:
            return get_kth_element(total // 2 + 1)
        else:
            return (get_kth_element(total // 2) + get_kth_element(total // 2 + 1)) / 2
