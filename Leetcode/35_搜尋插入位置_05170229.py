#題目敘述：给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
#如果目标值不存在于数组中，返回它将会被按顺序插入的位置，可以假设数组中无重复元素。

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
            

#採用最直觀的方式，判斷target是否存在於list
#存在直接顯示其排序，不存在則加入並排序list後再次尋找target並顯示排序
#結果：通過，用時44ms，消耗內存13.3MB
