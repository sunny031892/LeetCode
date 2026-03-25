# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        #用deque跑BFS
        queue = deque([root])
        level = 0

        #此迴圈一次處理一整層node
        while queue:
            #一層有幾個node
            size = len(queue)

            #初始值 偶數:負超大(遞增) 奇數:正超大(遞減)
            prev_val = float('-inf') if level % 2 == 0 else float('inf')

            for i in range(size):
                #popleft = front + pop
                node = queue.popleft()

                #偶數層
                if level % 2 == 0:
                    #數字奇數 + 嚴格遞增
                    if (node.val % 2 == 0) or (node.val <= prev_val):
                        return False
                #奇數層
                else:
                    #數字偶數 + 嚴格遞減
                    if (node.val % 2 != 0) or (node.val >= prev_val):
                        return False
                
                #更新比較值
                prev_val = node.val

                #下一層節點加入queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            #跳出while前層數加一
            level +=1
    
        return True
