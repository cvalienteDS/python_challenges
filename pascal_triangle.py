class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # start = 1
        ans = [[1]]
        for row in range(2, numRows + 1):
            row_data = [None] * row
            prev = [0] + ans[row-2] + [0]
            for cell in range(row):
                row_data[cell] = prev[cell] + (prev[cell+1])
                prev = row_data
            ans[0].append(row_data)

        return ans


sol = Solution().generate(numRows=5)
print(sol)

