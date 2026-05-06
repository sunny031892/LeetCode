class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        l = [1]
        while len(l) < n:
            odd = [2*num-1 for num in l if 2*num-1 <= n]
            even = [2*num for num in l if 2*num <= n]
            l = odd+even
        return l