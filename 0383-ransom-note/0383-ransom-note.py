from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        small_count=Counter(ransomNote)
        big_count=Counter(magazine)
        for char,coun in small_count.items():
            if big_count[char] < coun:
                return False
        return True

