class Solution(object):
    def Quick_sort(list): 
        a = [] #存放比key小的數值
        b = [] #存放比key大的數值
        c = [] #存放與key相同數值

    if len(list) <= 1:
        return list
    #若list僅一值不需排序

    else:
        key = list[0] #另第一個數為key
        for i in list:
            if i < key:
                a.append(i)
            elif i > key:
                b.append(i)
            else:
                c.append(i)

    #將兩邊數列再重複排序
    a = quick_sort(smaller)
    b = quick_sort(bigger)
    sort = a+c+b
    return sort
