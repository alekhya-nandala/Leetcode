class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i,value in enumerate(nums):
            differ=target-value
            if(differ in num_map):
                return [num_map[differ],i]
                            
            num_map[value]=i
           
