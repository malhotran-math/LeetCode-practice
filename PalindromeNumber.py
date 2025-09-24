class Solution:
    def isPalindrome(self, x: int) -> bool:
        checker = 0
        x = str(x) 
        n = len(x)
        while checker <= n/2:
            if x[checker] != x[n-checker-1]:
                return False
            else:
                checker += 1 
        return True
