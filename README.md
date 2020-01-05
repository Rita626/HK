# HomeWork(演算法筆記)

## 關於我
袁嘉謙 暱稱Rita、馬鈴薯~

目前擔任社企科技公司的行銷人員，

主要負責處理GA數據分析的部分。

## 僅用於2019演算法課程紀錄
紀錄108上學期演算法課程的點滴，
包含每次作業的程式碼內容，
以及各堂課的教學PPT和影片資源。

# Week1:
介紹課堂與工具

[上課影片](https://www.youtube.com/watch?v=LxvSt_jAWM4&feature=youtu.be)

[Codesignal](https://github.com/Rita626/HK/tree/master/Codesignal)

[Leetcode](https://github.com/Rita626/HK/tree/master/Leetcode)

[影片整理](https://github.com/Rita626/HK/tree/master/CS50)

# Week2
[Linked-list](https://docs.google.com/presentation/d/e/2PACX-1vRBr7b06XjLvDws-d-4ZjBCm_3aL_q3gKbKy2DRoOtIXwz-EApyndHBPbLme_e5V12ZNl1hDikuzEYW/pub?start=false&loop=false&delayms=3000&slide=id.p)

Linked-list是由一連串的節點（Node）所構成。

每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）

## 實作可以分成兩個類別（class）：

☆ 包含了資料及指標兩個屬性的節點（class ListNode）
 
☆ 定義出各種資料結構操作的list本身（class SingleLinkedList）

# Week3
[Stack&Queue](https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.p)

#Push將資料放入Stack(把書放進箱子)

#Pop把最上面的資料移除(把第一本書拿書來)

#Top回傳最上面的資料(確認箱子最上面的書)

#IsEmpty確認Stack是否有資料(確認箱中是否有書)

#getSize回傳資料個數(紀錄箱子裡裝多少書)

# Week4
[Insertion Sort](https://docs.google.com/presentation/d/e/2PACX-1vQOTMDM-5-OUaGfnLUOFVgefFwSVRplSwnbicp0CXOQrB5H8RM_1Aq8o_4JxHlncEmhjvqk3tzcoB7s/pub?start=false&loop=false&delayms=3000&slide=id.p)

# Week5
[Quick Sort](https://docs.google.com/presentation/d/e/2PACX-1vSqz8sTxT4xyjgiz-htLvZd7FZ_5ZzgKf60pFEoNLU5S77JxrsGJ2vd15CdxlfLtT3g2aizHP-Ebk9b/pub?start=false&loop=false&delayms=3000&slide=id.p)

[作業一](https://github.com/Rita626/HK/blob/master/HW1/1004_QuickSort.ipynb)

#左找大右找小

#取第一個元素（最左的數）為鍵值 key

#由左向右（前向後）找一個數（第一個滿足的），其值大於等於 key 值，該數之索引為 left_pivot

#由右向左（後向前）找一個數（第一個滿足的），其值小於等於 key 值，該數之索引為 right_pivot

#如果 left_pivot < right_pivot 則交換值，否則把 key 值與 right_pivot 值交換，以 right_pivot 為基準，分為左右兩個數列

#重複上述步驟排序左右兩個數列，直到完成排序

# Week6
[Heap Sort](https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.p)

[作業二](https://github.com/Rita626/HK/blob/master/HW2/heap_sort_05170229.py)

[流程](https://github.com/Rita626/HK/blob/master/HW2/HeapSort_%E6%B5%81%E7%A8%8B%E5%9C%96%E6%AD%B7%E7%A8%8B%E8%88%87%E8%AA%AA%E6%98%8E.pdf)

# Week7
[Merge Sort](https://docs.google.com/presentation/d/e/2PACX-1vToxkEzc1H1RT5MI9G941KQFBC7GO_Efn95wTqXLEdr3LDBSNcQb-M46IOC-_RzZih6IBEwwy3rWQuE/pub?start=false&loop=false&delayms=3000&slide=id.p)

[作業二](https://github.com/Rita626/HK/blob/master/HW2/merge_sort_05170229.py)

[流程](https://github.com/Rita626/HK/blob/master/HW2/MergeSort_%E6%B5%81%E7%A8%8B%E5%9C%96%E6%AD%B7%E7%A8%8B%E8%88%87%E8%AA%AA%E6%98%8E.pdf)

[比較](https://github.com/Rita626/HK/blob/master/HW2/HeapSort_MergeSort_%E6%AF%94%E8%BC%83.pdf)

# Week8
[Binary Tree](https://docs.google.com/presentation/d/e/2PACX-1vSC3P8sGElP48mJTjqT309470SmTFBwJXWsU9hTX2hg5tVpiG4yC703qA7ibPep-Qakmm2Mw_F-ScZh/pub?start=false&loop=false&delayms=3000&slide=id.p)

[作業三](https://github.com/Rita626/HK/blob/master/HW3/binary_search_tree_05170229.py)

[流程](https://github.com/Rita626/HK/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86_05170229.pdf)

[功能](https://github.com/Rita626/HK/blob/master/HW3/Binary_Search_Tree%E6%96%B0%E5%A2%9E%E3%80%81%E6%9F%A5%E8%A9%A2%E3%80%81%E5%88%AA%E9%99%A4%E3%80%81%E4%BF%AE%E6%94%B9%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E_05170229.pdf)

# Week9
[AWS區塊練介紹](https://www.youtube.com/watch?v=1aWQz5PemHY&feature=youtu.be)

# Week10
[Red Black Tree](https://docs.google.com/presentation/d/e/2PACX-1vRxyJRARq0BNuGJq_o2cUHIXBWrRSZrAOyXOSt9qCTSjQtyp8XqFq3VuNn3gCt3sXenOZmWLqIjcyFs/pub?start=false&loop=false&delayms=3000&slide=id.p)

# Week11
[Hash Table](https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.p)

[作業四](https://github.com/Rita626/HK/blob/master/HW4/hash_table_05170229.py)

[流程](https://github.com/Rita626/HK/blob/master/HW4/HashTable_HashFunction_%E5%8E%9F%E7%90%86%E6%B5%81%E7%A8%8B05170229.pdf)

# Week12
[BFS](https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p)

# Week13
[DFS](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.p)

[BFS DFS流程&比較](https://github.com/Rita626/HK/blob/master/HW5/BFS_DFS_%E5%8E%9F%E7%90%86%E6%B5%81%E7%A8%8B05170229.pdf)

# Week14
[Minimum Spanning Tree](https://docs.google.com/presentation/d/e/2PACX-1vTorNDEyhYA4ZAt5jEqOmFs2cQiUAYvkTp-R0DOn9B3c1MuUecV-a1wNakFIrJxA6AoUFGzbl3OQBIJ/pub?start=false&loop=false&delayms=3000&slide=id.p)

# Week15
[Shortest Path](https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.p)

[作業六](https://github.com/Rita626/HK/blob/master/HW6/Dijkstra_05170229.py)

[Minimum Spanning Tree & Shortest Path流程](https://github.com/Rita626/HK/blob/master/HW6/Kruskal_Dijkstra_%E5%8E%9F%E7%90%86%E6%B5%81%E7%A8%8B05170229.pdf)

# 心得
不得不說，這堂課所教的內容真的非常豐富，

可惜對我來說，如果選的時間能在一兩年前就好了，

現在我的工作主要是以行銷為主，

每周不停在理性腦與感性腦中做切換時常轉不過來...

且時常好不容易寫出一些東西卻無法運作，

與工作時的游刃有餘相比在這堂課上真的挺苦惱與挫敗，

不過對未來要走coding這方面的人而言這門課絕對是非常受用的。
