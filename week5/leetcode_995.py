class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()  # 這裡面存的是「所有還在發揮作用的翻轉起始座標」
        res = 0      # 總翻轉次數
        
        for i, num in enumerate(nums):
            # 1. 檢查隊首的翻轉是否過期
            # (i - q[0] + 1) 就是這個翻轉涵蓋的長度
            # 如果大於 k，代表 i 已經超出這個翻轉的控制範圍了，直接踢掉
            while q and (i - q[0] + 1) > k:
                q.popleft()
            
            # 2. 判斷現在這個位置要不要翻轉
            # len(q) 代表「目前有多少個翻轉同時覆蓋在 i 這個點上」
            # 如果 (翻轉次數 + 原始數值) 是偶數，代表目前這裡是 0，必須翻轉
            # 舉例：num=0，len(q)=0 (偶數) -> 0+0=0，要翻
            # 舉例：num=1，len(q)=1 (奇數) -> 1+1=2，要翻
            if (len(q) + num) % 2 == 0:
                # 剩餘長度不夠 k，無法翻轉，宣告失敗
                if i + k > len(nums):
                    return -1
                
                # 確定翻轉，紀錄次數，並把這次翻轉的起始位置放進 q
                res += 1
                q.append(i)
                
        return res