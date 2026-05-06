class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # 把每一棟建築拆成 開始 跟 結束 兩個時間點
        # 高度寫成負的是為了讓python的min heap變max heap來用
        # 排序規則：x 小的在前，x 一樣時，高的在前（負值小的在前）
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))  # 這裡帶上右邊界r，方便後面判斷過期
            events.append((r, 0, 0))   # 結束點的高度設為0
        
        events.sort()
        
        # 用一個不可能出現的x當作初始值
        # 這樣第一個建築物進來時，就不會因為 x=0 跟初始點重疊而被切掉
        res = [[-1, 0]]
        
        # heap裡放 (負高度, 右邊界)，先塞個地平線進去墊底
        live_max_heap = [(0, float('inf'))]
        
        for x, neg_h, r in events:
            # 遇到新的建築開始，直接丟進 heap
            if neg_h < 0:
                heapq.heappush(live_max_heap, (neg_h, r))
            
            # 這是最核心的一步：把那些已經「走入歷史」的建築從 heap 頂端清掉
            # 只要頂端建築的右邊界 <= 現在的 x，就代表它已經不影響現在的天際線了
            while live_max_heap[0][1] <= x:
                heapq.heappop(live_max_heap)
            
            # 看看現在最高的高度是多少
            curr_max_h = -live_max_heap[0][0]
            
            # 如果現在的高度跟上一個點的高度不一樣，代表轉折了
            if res[-1][1] != curr_max_h:
                # 處理同一個 x 座標有連續多個事件的情況
                if res[-1][0] == x:
                    res[-1][1] = curr_max_h
                else:
                    res.append([x, curr_max_h])
        
        # 把當初那個為了初始化而放的 [-1, 0] 丟掉
        return res[1:]