# HomeWork(演算法筆記)

## 關於我
袁嘉謙 暱稱Rita、馬鈴薯~

目前擔任社企科技公司的行銷人員，

主要負責處理GA數據分析的部分。

## 僅用於2019演算法課程紀錄
認為學習的目的在於學到方法，至於在理論與程式邏輯皆相同的情況下，

硬是要使程式碼寫的與普羅大眾不同，用以證明並非抄襲，對此仍抱持著觀察的態度。

# Week1:
介紹課堂與工具
[上課影片].(https://www.youtube.com/watch?v=LxvSt_jAWM4&feature=youtu.be)

# Week2
Linked-list是由一連串的節點（Node）所構成。

每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）

## 實作可以分成兩個類別（class）：

☆ 包含了資料及指標兩個屬性的節點（class ListNode）
 
☆ 定義出各種資料結構操作的list本身（class SingleLinkedList）

# Stack(後進先出)
#Push將資料放入Stack(把書放進箱子)

#Pop把最上面的資料移除(把第一本書拿書來)

#Top回傳最上面的資料(確認箱子最上面的書)

#IsEmpty確認Stack是否有資料(確認箱中是否有書)

#getSize回傳資料個數(紀錄箱子裡裝多少書)

# Quick Sort(左找大右找小)
#取第一個元素（最左的數）為鍵值 key

#由左向右（前向後）找一個數（第一個滿足的），其值大於等於 key 值，該數之索引為 left_pivot

#由右向左（後向前）找一個數（第一個滿足的），其值小於等於 key 值，該數之索引為 right_pivot

#如果 left_pivot < right_pivot 則交換值，否則把 key 值與 right_pivot 值交換，以 right_pivot 為基準，分為左右兩個數列

#重複上述步驟排序左右兩個數列，直到完成排序
