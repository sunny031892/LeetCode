class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        # 整理式子後得 (y_i - x_i) + (y_j + x_j)
        # dq 裡面存 (y - x, x)，並且保持 y - x 是由大到小排序
        dq = deque()
        max_val = float('-inf')
        
        for x, y in points:
            # 1. 先把離太遠、不符合條件的點從前面踢掉
            while dq and x - dq[0][1] > k:
                dq.popleft()
            
            # 2. 如果隊列還有剩，隊首就是目前最好的候選點 i
            if dq:
                max_val = max(max_val, dq[0][0] + x + y)
            
            # 3. 準備把現在這個點當作未來的候選點 i 放進去
            # 放進去前，把隊尾 y-x 比我小的人都踢了，因為我比他們強又比他們晚過期
            curr_val = y - x
            while dq and dq[-1][0] <= curr_val:
                dq.pop()
            
            dq.append((curr_val, x))
            
        return max_val