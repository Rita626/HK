#題目：给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = [j for j in range(0, len(nums)+1)]
        b = []
        nums.sort()
        for i in a:
            if i in nums:
                b.append(i)
                a.remove(i)
        return a[0]

#想法:先做出一個無缺失值的列表，接著比對兩者，有重複則移除，並放入另一個空間，最終剩下的即為遺漏值
#結果：答案錯誤...
