#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object): 
    
    #新增資料
    def insert(self, root, val):        
        if root == None:
            root = TreeNode(val)
            return root
        elif val <= root.val:
            if root.left == None:
                root.left = TreeNode(val)
                return root.left
            else:
                root = root.left
                #原先return到root.left一直出錯，發現是迴圈順序會有錯
                return self.insert(root, val)                
        elif val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
                return root.right
            else:
                root = root.right
                #原先return到root.right一直出錯
                return self.insert(root, val)
            
    #搜尋資料        
    def search(self, root, target):
        if root == None or root.val == target:
            return root
        elif root.val > target:
            root = root.left
            return self.search(root, target)
        else:
            root = root.right
            return self.search(root, target)
        
        
    #刪除資料        
    def delete(self, root, target):
        
        head = None
        need = root
        
        while need != None and need.val != target:
            head = need
            if target < need.val:
                need = need.left
            else:
                need = need.right
        if need == None:
            return root
        
        #查無值
        get = self.search(root, target)
        if get == None:
            return get
        
        #無節點
        elif need.left == None and need.right == None:
            if need != root:
                if head.left == need: #原先打一個"="無法運作
                    head.left == None
                else:
                    head.right == None
            else:
                root == None
                
        #一個節點        
        elif need.left == None and need.right != None:
            after = need.right
            if need != root:
                if head.left == need:
                    head.left = after
                else:
                    head.right = after
            else:
                root = after
                
        elif need.right == None and need.left != None:
            after = need.left
            if need != root:
                if head.left == need:
                    head.left = after
                else:
                    head.right = after
            else:
                root = after
        
        #2個節點
        else:
            after = need.left
            if need != root:
                if head.left == need:
                    head.left = after
                else:
                    head.right = after
            else:
                root = after
        
        #再搜尋過是否有重複值
        if self.search(root, target) != None:
            self.delete(root, target)
        return root
    
    #修改
    def modify(self, root, target, new_val):
        
        #先確認是否有被修改值
        if root == None:
            root = TreeNode(new_val)
            
        elif self.search(root, target) == None:
            self.insert(root, new_val)
            
        else:
            self.delete(root, target)
            self.insert(root, new_val)
        return root            


# In[3]:


root = TreeNode(5)
Solution().insert(root,3)
Solution().insert(root,3)
Solution().insert(root,-5)
Solution().insert(root,8)
Solution().insert(root,7)
Solution().insert(root,6)
Solution().insert(root,10)


# In[7]:


print(Solution().insert(root,4)==root.left.right)


# In[4]:


print(Solution().search(root,0)==root.right.right)


# In[5]:


root2 = Solution().delete(root,3)
print(root2.val==5 and root2.left.val==-5 and root2.left.left==None and root2.left.right==None)
print(root2.right.right.val==10 and root2.right.left.val==7 and root2.right.left.left.val==6)
print(root2.right.right.right==None and root2.right.right.left==None and root2.right.left.right==None)
print(root2.right.left.left.left==None and root2.right.left.left.right==None and root2.right.val==8)


# In[4]:


root4 = Solution().modify(root, 7, 4)
print(isBinarySearchTree(root4))

