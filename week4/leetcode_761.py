class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # 既然是遞迴，空字串就直接回傳
        if not s:
            return ""
        
        count = 0  # 用來算 1 和 0 的差額，就像在做括號匹配
        i = 0      # 記錄每一段特殊字串的起點
        res = []   # 用來存拆出來的各個「包裹」
        
        for j in range(len(s)):
            # 看到 1 就加 1，看到 0 就減 1
            if s[j] == '1':
                count += 1
            else:
                count -= 1
            
            # 當 count 歸零，代表我們抓到一個完整的「特殊字串」包裹了
            if count == 0:
                # 重點：這個包裹一定是以 1 開頭、0 結尾
                # 我們把頭尾去掉，對中間的東西做遞迴排序
                # 處理完後再把頭尾 1 和 0 補回去
                inner_part = self.makeLargestSpecial(s[i+1:j])
                res.append("1" + inner_part + "0")
                
                # 更新下一個包裹的起點
                i = j + 1
        
        # 拿到所有處理好的包裹後，由大到小排個序
        # 字串排序剛好符合我們要的字典序
        res.sort(reverse=True)
        
        # 把排好的包裹接起來就是答案啦
        return "".join(res)