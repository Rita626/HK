#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###### merge_sort_ID.py

class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """


# In[15]:


class Solution(object):
    def merge_sort(self, nums):
        self.nums = nums
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]
        Sorted = Solution().sort(nums)
        return Sorted
    
    
    #先切割
    def cut(self, nums):
        cutcut = len(nums)//2
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]
    
    #再合併
    def merge(left, right):
        if len(left) == 0:
            return right
        elif len(right) == 0:
            return left
        
        index_left = index_right = 0
        merged = []
        lentarget = len(left) + len(right)
        
        while len(merged) < lentarget:
            if left[index_left] <= right[index_right]:
                merged.append(left[index_left])
                index_left += 1
            else:
                merged.append(right[index_right])
                index_right += 1
            if index_right == len(right):
                merged += left[index_left:]
                break
            elif index_left == len(left):
                merged += right[index_right:]
                break
            return merged
        
    def sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            left, right = Solution().cut(nums)
            return (sort(left), sort(right))
        
#還在思考邏輯的部分


# In[16]:


output=Solution().merge_sort([3,5,-9,6,8])
output


# In[ ]:




