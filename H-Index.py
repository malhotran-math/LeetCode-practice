class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hI = 0
        for i in citations: 
            count = sum(1 for cite in citations if cite>= i)
            if count >= i:
                hI = i
        return hI    
