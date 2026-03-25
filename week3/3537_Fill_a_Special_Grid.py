class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        # 初始化 2^n x 2^n 的網格
        size = 1 << n
        res = [[0] * size for _ in range(size)]
        
        def fill(r, c, s, val):
            # 遞迴終止：填入單一數值
            if s == 1:
                res[r][c] = val
                return
            
            # 將網格切半，計算每個子象限的元素數量
            half = s // 2
            q_size = half * half
            
            # 依照題目要求的大小順序遞迴填充
            # 1. 右上 (Top-Right) 最小
            fill(r, c + half, half, val)
            
            # 2. 右下 (Bottom-Right) 次之
            fill(r + half, c + half, half, val + q_size)
            
            # 3. 左下 (Bottom-Left) 再次之
            fill(r + half, c, half, val + 2 * q_size)
            
            # 4. 左上 (Top-Left) 最大
            fill(r, c, half, val + 3 * q_size)
            
        fill(0, 0, size, 0)
        return res