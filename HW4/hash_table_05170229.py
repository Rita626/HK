#!/usr/bin/env python
# coding: utf-8

# In[9]:


from Cryptodome.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    #先進行MD5加密
    def add(self, key):
        md5 = MD5.new()
        md5.update(key.encode("utf-8"))
        md5 = md5.hexdigest()
        #採用餘數存取
        bucket = int(md5)
        #若有相同的則用link list
        if self.data[bucket] == None:
            self.data[bucket] = ListNode(md5)
        else:
            new = ListNode(md5)
            first = self.data[bucket]
            while first.next != None:
                first = first.next
            first.next = new
            
    def remove(self, key):
        md5 = MD5.new()
        md5.update(key.encode("utf-8"))
        md5 = md5.hexdigest()
        bucket = int(md5)
        delete = self.data[bucket]
        num = delete
        if delete != None:
            if delete.next != None:
                if delete.val == h:
                    self.data[bucket] = delete.next
                else:
                    num = delete
                    while delete.next:
                        if delete == md5:
                            num.next = delete.next
                        else:
                            num = delete
                            delete = delete.next
            else:
                if delete.val == md5:
                    self.data[bucket] = None
        if self.contains(key) == True:
            self.remove(key)
            
    def contains(self, key):
        md5 = MD5.new()
        md5.update(key.encode("utf-8"))
        md5 = md5.hexdigest()
        bucket = int(md5)
        if self.data[bucket] != None:
            node = self.data[bucket]
            while node.next != None:
                node = node.next
                if node.val == h:
                    break
            if node.val == h:
                return True
            else:
                return False
        else:
            return False


# In[11]:


#MyHashSet().add('rita')

