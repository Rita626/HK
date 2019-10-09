# HomeWork(演算法筆記)

僅用於2019演算法課程紀錄，一個只會寫python，不懂演算法的艱苦人生

# Linked list

Linked-list是由一連串的節點（Node）所構成，每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）。
實作可以分成兩個類別（class），一個是包含了資料及指標兩個屬性的節點（class ListNode），另一個則是定義出各種資料結構操作的list本身（class SingleLinkedList）。

# Stack
用Push將資料放入Stack(把書放進箱子)，Pop把最上面的資料移除(把第一本書拿書來)，Top回傳最上面的資料(確認箱子最上面的書)，IsEmpty確認Stack是否有資料(確認箱中是否有書)，getSize回傳資料個數(紀錄箱子裡裝多少書)。

# Quick Sort

先找出節點，將資料分大小兩邊放，再從兩邊各找一個節點，同樣各把資料分兩邊放，不斷重複直到分完。
