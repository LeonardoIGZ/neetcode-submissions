class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        pascal_triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            row = []
            row.append(1)
            for j in range(len(pascal_triangle[i-1]) - 1):
                value = pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j + 1] 
                row.append(value)
            row.append(1)
            pascal_triangle.append(row)
        return pascal_triangle