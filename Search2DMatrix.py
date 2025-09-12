import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # A naive approach, runs in O(m*n) complexity
        #mat = np.array(matrix)
        #mat.flatten()
        #check = target in mat
        #return check

        # The next approach is O(log(m*n)), but assumes the matrix is sorted
        m, n = len(matrix), len(matrix[0]) #rows and columns 
        start, end = 0, m*n-1 #ends for binary search 
        while start <= end: 
            mid = (start+end)//2 
            midval = matrix[mid//n][mid % n]
            if target == midval :#we don't flatten the matrix, just search row wise 
                return True 
            elif target > midval: 
                start = mid #search the second half
            else:
                end = mid #search the first half
        return False
