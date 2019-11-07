#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##### heap_sort_ID.py

class Solution(object):
    def heap_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """


# In[46]:


class Solution(object):
    #最後要出來的結果
    def heap_sort(self,nums): 
        self.nums = nums
        Sorted = Solution().sort(nums)
        return Sorted
    
    #最重要的排序，比較元素的大小
    def heapify(self, nums, n, i):
        left = 2 * i + 1  
        right = 2 * (i + 1)   
        Max = i   
        
        if left < n and nums[i] < nums[left]:   
            Max = left   
        if right < n and nums[Max] < nums[right]:   
            Max = right   
        if Max != i:   
            nums[Max], nums[i] = nums[i], nums[Max]   
            Solution().heapify(nums, n, Max) 

    #讓最後值消失的概念，然後與最後交換再做maxheap，這個步驟一直出錯
    def sort(self,nums):
        end = len(nums)   
        start = end // 2 - 1
        for i in range(start, -1, -1):   
            Solution().heapify(nums, end, i)  #Solution一直漏加 
        for i in range(end-1, 0, -1):   
            nums[0], nums[i] = nums[i], nums[0]   
            Solution().heapify(nums, i, 0)   
        return nums 


# In[47]:


output=Solution().heap_sort([3,5,-9,6,8])
output
#試了好多次才成功...
#寫完去翻才發現和老師的爆像...算了改天再看怎麼把它變不一樣

