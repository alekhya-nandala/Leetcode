class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        n=words[len(words)-1]
        return (len(n))