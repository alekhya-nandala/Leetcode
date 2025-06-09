class Solution:
    def isPalindrome(self, s: str) -> bool:
        v=''.join(c.lower() for c in s if c.isalnum())
        b=v[::-1]
        if v==b:
            return True
        else:
            return False
        