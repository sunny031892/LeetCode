class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, start, end):
        if start >= end:
            return 0
        
        mid = (start + end) // 2
        # 遞迴計算左右兩半的對數
        cnt = self.mergeSort(nums, start, mid) + self.mergeSort(nums, mid + 1, end)
        
        # 計算跨左右兩區的反向對
        j = mid + 1
        for i in range(start, mid + 1):
            # 找到第一個不滿足 2倍 條件的位置
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            # j之後的數字都不符條件 故累積 j 扣掉右區起始位置
            cnt += j - (mid + 1)
        
        # 合併排序好的子陣列
        nums[start:end+1] = sorted(nums[start:end+1])
        return cnt