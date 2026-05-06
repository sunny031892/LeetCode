class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        # 1. 把速度跟效率綁在一起，按效率「從大到小」排好
        # 這樣當我們掃到某人時，他就是目前團隊裡效率最差的那個
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        min_heap = []
        speed_sum = 0
        max_perf = 0
        
        for e, s in engineers:
            # 2. 把當前工程師的速度加進去
            speed_sum += s
            heapq.heappush(min_heap, s)
            
            # 3. 如果人數超過 k，就把速度最慢（堆積頂端）的踢掉
            # 因為我們要的是在目前效率限制下，總速度越快越好
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
            
            # 4. 計算表現：目前的總速度 * 目前這位工程師的效率（他是目前最菜的）
            max_perf = max(max_perf, speed_sum * e)
            
        return max_perf % (10**9 + 7)