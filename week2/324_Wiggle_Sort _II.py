class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 複製並排序原陣列
        arr = sorted(nums)
        n = len(nums)
        
        # 計算左半部(較小區)的最後一個索引
        # 使用 (n-1)//2 確保奇偶長度都能正確分割
        mid = (n - 1) // 2
        
        # 指標分別指向左半部與右半部的末端
        left = mid
        right = n - 1
        
        # 建立暫存結果，避免覆蓋尚未讀取的數字
        res = [0] * n
        
        for i in range(n):
            if i % 2 == 0:
                # 偶數索引放入左半部較大的數字
                res[i] = arr[left]
                left -= 1
            else:
                # 奇數索引放入右半部較大的數字
                res[i] = arr[right]
                right -= 1
        
        # 將結果複製回原陣列
        nums[:] = res