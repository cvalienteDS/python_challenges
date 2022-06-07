from typing import List

class Solution(object):
    # def matrixReshape(self, mat, r, c):
    #     """
    #     :type mat: List[List[int]]
    #     :type r: int
    #     :type c: int
    #     :rtype: List[List[int]]
    #     """
    #     reshaped_mat = []
    #     temp = []
    #
    #     for row in mat:
    #         for cell in row:
    #             temp.append(cell)
    #     if len(temp) != (r*c):
    #         return mat
    #
    #     counter = 0
    #     for i in range(r):
    #         col = []
    #         for j in range(c):
    #             col.append(temp[counter])
    #             counter += 1
    #         reshaped_mat.append(col)
    #     return reshaped_mat

    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if nums == [] or r * c != len(nums) * len(nums[0]):
            return nums

        ans = [[0 for j in range(c)] for i in range(r)]
        k = None

        for row in nums:
            for num in row:
                ans[k // c][k % c] = num
                k += 1

        return ans


sol = Solution().matrixReshape([[1, 2], [3, 4]], r=1, c=4)

