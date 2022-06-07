class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            ix = left + (right - left) // 2
            guess = nums[ix]
            if guess == target:
                return ix
            if target < guess:
                right = ix - 1
            if target > guess:
                left = ix + 1
        return -1


instance = Solution()
instance.search(nums=list(range(9)), target=6)