import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = np.array(matrix)
        mat.flatten()
        check = target in mat
        return check
