import heapq
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0

        # arr 複製一份 nums，方便後續合併數值
        arr = [int(x) for x in nums]
        removed = [False] * n
        heap = []
        
        # 建立陣列版的雙向鏈結串列：pre 存左鄰居，nxt 存右鄰居
        pre = [i - 1 for i in range(n)]
        nxt = [i + 1 for i in range(n)]
        nxt[-1] = -1 # 最後一個人的右邊設為 -1 代表沒人

        # 判定一對鄰居有沒有排好 (左邊 <= 右邊)
        def is_sorted(i, j):
            if i == -1 or j == -1: return 0
            return 1 if arr[i] <= arr[j] else 0

        # 1. 初始點名：算一下全場目前有幾對是排好的
        asc = 0
        for i in range(n - 1):
            # 存入 heap：(總和, 左邊 index)
            heapq.heappush(heap, (arr[i] + arr[i+1], i))
            asc += is_sorted(i, i + 1)
            
        # 如果一開始就排好了，直接回傳 0
        if asc == n - 1: return 0

        rem = n # 剩餘元素數量
        
        while heap:
            sumv, left = heapq.heappop(heap)
            right = nxt[left]

            # 懶惰刪除檢查：如果鄰居關係變了，或總和不對，代表是舊資料
            if right == -1 or removed[left] or removed[right] or nxt[left] != right or arr[left] + arr[right] != sumv:
                continue

            # 準備合併
            p = pre[left]
            a = nxt[right]

            # --- 合併前：先扣掉受影響的 3 組鄰居關係 ---
            asc -= is_sorted(p, left)
            asc -= is_sorted(left, right)
            asc -= is_sorted(right, a)

            # --- 執行合併 ---
            arr[left] += arr[right]
            removed[right] = True
            rem -= 1 # 總人數減 1

            # --- 重新接線 ---
            nxt[left] = a
            if a != -1:
                pre[a] = left
            
            # --- 合併後：加上受影響的 2 組新關係 ---
            asc += is_sorted(p, left)
            asc += is_sorted(left, a)

            # 檢查是否已經全陣列排序 (剩餘 rem 個元素，應有 rem-1 對排好)
            if asc == rem - 1:
                return n - rem

            # 把受影響的新數對丟回 heap 重新排隊
            if p != -1:
                heapq.heappush(heap, (arr[p] + arr[left], p))
            if a != -1:
                heapq.heappush(heap, (arr[left] + arr[a], left))

        return n - 1