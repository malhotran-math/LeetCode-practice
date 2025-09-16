class Solution:
    def isHappy(self, n: int) -> bool:
        while n>9:
            digits = len(str(abs(n)))
            tot = 0 
            for i in range(digits):
                digit = n%10 
                n //= 10 
                tot+= digit**2
            if tot == 1: 
                return True 
            elif 1<tot<10:
                return False 
            n = tot
        return n==1

        
