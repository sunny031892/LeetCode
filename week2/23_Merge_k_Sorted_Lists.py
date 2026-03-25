# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 建立虛擬頭節點方便操作
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        # 將所有非空串列的首節點存入 Heap
        # 存入格式: (節點值, 索引序號, 節點物件)
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        while heap:
            # 取得當前最小值節點
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # 若該串列還有後續節點 則繼續放入 Heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next