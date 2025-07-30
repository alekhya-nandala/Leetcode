class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[-1])
        total_count=0
        for boxtype,units_per_box in boxTypes:
            if truckSize==0:
                break
            
            boxes=min(truckSize,boxtype)
            total_count+=boxes*units_per_box
            truckSize-=boxes
        return total_count