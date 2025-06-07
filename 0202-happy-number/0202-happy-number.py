class Solution:
    def isHappy(self, n: int) -> bool:
        v = set()
        while n != 1:
            if n in v:
                return False
            v.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return True
