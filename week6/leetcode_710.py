import random

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        # 1. 算出有效範圍 W
        self.w = n - len(blacklist)
        self.mapping = {}
        
        # 把黑名單轉成 set
        black_set = set(blacklist)
        
        # 2. 找出黑區裡合法的數字有哪些
        # 從n-1開始往回找，找 len(blacklist) 個候選位
        last = n - 1
        
        # 我們只處理在白區內的黑名單
        for b in blacklist:
            if b < self.w:
                # 找一個黑區裡的合法數字來遞補
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        # 在 [0, W-1] 隨機抽號
        idx = random.randint(0, self.w - 1)
        # 如果抽到黑名單，就回傳映射後的合法數字；否則直接回傳
        return self.mapping.get(idx, idx)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()