class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = len(n)
        while left < right:
            pivot = left + (right - left) // 2
            guess = versions[pivot]
            if guess is True:
                right = pivot
            if guess is False:
                left = pivot + 1
        return pivot + 1


# versions = {1:False, 2:False, 3:False,4:False, 5:False,6:False, 7:True,8:True, 9:True}
versions = {1:False, 2:True, 3:True}
instance = Solution()
output = instance.firstBadVersion(n=versions)
print(output)