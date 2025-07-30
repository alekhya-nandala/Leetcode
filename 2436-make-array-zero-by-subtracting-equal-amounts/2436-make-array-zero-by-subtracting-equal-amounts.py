class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l=set()
        for num in nums:
            if num>0:
                l.add(num)

        return len(l)
        