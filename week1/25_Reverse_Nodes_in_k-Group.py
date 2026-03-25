# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #提取所有數值存進vals
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        #每k個一組反轉數值
        n = len(vals)
        #從0開始每次跳k格 直到湊不下一組
        for i in range(0, n - n % k, k):
            #把這一段提出來
            sub_list = vals[i:i+k]
            
            #做原地反轉
            sub_list.reverse()
            
            #再把反轉後的小清單塞回原本的位置
            vals[i:i+k] = sub_list
        
        #把反轉後的數值塞回去原本的node
        curr = head
        for v in vals:
            curr.val = v
            curr = curr.next
            
        return head