#題目：给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
            
#想法：很直觀的直接搜尋了...
#結果：通過，用時288ms，內存消耗13.9MB

#不過這個做法貌似不符合題意...預備再重解
