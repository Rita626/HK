#題目：给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None or root.val == val:
            return root
        elif root.val > val:
            root = root.left
            return self.searchBST(root, val)
        else:
            root = root.right
            return self.searchBST(root, val)
            
#想法：從root開始比較起，若搜尋值<root則往左，反之則往右。(此題是這學期學的，之前HW3寫過，所以寫起來蠻順利)
#結果：通過，用時84ms，內存消耗18.7MB
