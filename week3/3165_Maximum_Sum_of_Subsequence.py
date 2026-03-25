class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        tree = [[0] * 4 for _ in range(4 * n)]
        
        def build(tidx, lo, hi):
            if lo == hi:
                tree[tidx][0] = max(0, nums[lo])
            else:
                mid = (lo + hi) // 2
                build(2 * tidx + 1, lo, mid)
                build(2 * tidx + 2, mid + 1, hi)
                l0h0A, l1h0A, l0h1A, l1h1A = tree[2 * tidx + 1]
                l0h0B, l1h0B, l0h1B, l1h1B = tree[2 * tidx + 2]
                # lo to hi
                tree[tidx][0] = max(l0h1A + l1h0B, l0h0A + l1h0B, l0h1A + l0h0B)
                # lo + 1 to hi
                tree[tidx][1] = max(l1h1A + l1h0B, l1h0A + l1h0B, l1h1A + l0h0B)
                # lo to hi - 1
                tree[tidx][2] = max(l0h1A + l1h1B, l0h0A + l1h1B, l0h1A + l0h1B)
                # lo + 1 to hi - 1
                tree[tidx][3] = max(l1h1A + l1h1B, l1h0A + l1h1B, l1h1A + l0h1B)
        
        build(0, 0, n - 1)
        
        def update(tidx, lo, hi, i, val):
            if lo == hi:
                tree[tidx][0] = max(0, val)
            else:
                mid = (lo + hi) // 2
                if i > mid:
                    update(tidx * 2 + 2, mid + 1, hi, i, val)
                else:
                    update(tidx * 2 + 1, lo, mid, i, val)
                l0h0A, l1h0A, l0h1A, l1h1A = tree[2 * tidx + 1]
                l0h0B, l1h0B, l0h1B, l1h1B = tree[2 * tidx + 2]
                # lo to hi
                tree[tidx][0] = max(l0h1A + l1h0B, l0h0A + l1h0B, l0h1A + l0h0B)
                # lo + 1 to hi
                tree[tidx][1] = max(l1h1A + l1h0B, l1h0A + l1h0B, l1h1A + l0h0B)
                # lo to hi - 1
                tree[tidx][2] = max(l0h1A + l1h1B, l0h0A + l1h1B, l0h1A + l0h1B)
                # lo + 1 to hi - 1
                tree[tidx][3] = max(l1h1A + l1h1B, l1h0A + l1h1B, l1h1A + l0h1B)
        
        ans = 0
        for i, x in queries:
            update(0, 0, n - 1, i, x)
            ans += max(tree[0])
        return ans % 1_000_000_007