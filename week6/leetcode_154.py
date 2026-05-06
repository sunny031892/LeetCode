class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l + r) // 2

            # 情況 1：中間比右邊大，表示最小值在右半部（大的變小）
            if nums[mid] > nums[r]: 
                l = mid + 1

            # 情況 2：中間比右邊小，表示最小值在左半部（包含 mid 自己）
            elif nums[mid] < nums[r]: 
                r = mid

            # 情況 3：中間等於右邊，無法判斷，把右邊界往左縮一格（反正一樣）
            else: 
                r -= 1
                
        return nums[l] # 最後 l 和 r 會相遇在最小值點