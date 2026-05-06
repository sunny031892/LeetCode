class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        # 初始狀態：每個人先發 1 顆糖果
        candies = [1] * n
        
        # 第一輪：從左往右掃
        # 如果我比左邊的人分數高，我就要比他多拿一顆
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # 第二輪：從右往左掃
        # 如果我比右邊的人分數高，我要確保我的糖果比他多
        # 這裡用 max 是為了不破壞第一輪已經建立好的「比左邊多」的規則
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        # 把所有人手上的糖果加起來就是答案
        return sum(candies)