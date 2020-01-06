#題目：给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = []
        for i in nums:
            if i in a:
                a.remove(i)
            else:
                a.append(i)
        return a[0]
        
#類似配對遊戲的概念，拿一個空的籃子，並將列表中的每個值都提出來看，若籃子中沒有那個值則把值放進去
#若籃子中已經有了同樣值則將值拿出，當每個值都取出比對過，最後剩下的便會是只出現一次的值

#結果：通過，用時1436ms，內存消耗15.2MB
