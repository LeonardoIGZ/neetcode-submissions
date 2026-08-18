class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # my tab sizes
        row_size = len(board)
        column_size = len(board[0])

        # column support
        col_elements = [set() for _ in range(row_size)]

        # board support
        box_elements = [set() for _ in range(row_size)]

        for i in range(row_size):
            row_elements = set()

            for j in range(column_size):
                cell_value = board[i][j]
                
                if cell_value != '.':  
                    # row search
                    is_valid_row = self.isValidPosition(cell_value, row_elements)
                    if not is_valid_row:
                        return False

                    # column search
                    is_valid_column = self.isValidPosition(cell_value, col_elements[j])
                    if not is_valid_column:
                        return False

                    # box search
                    box_position = self.getBox(i, j)
                    is_valid_box = self.isValidPosition(cell_value, box_elements[box_position])
                    if not is_valid_box:
                        return False
        return True

    # validates existence of an item on a set
    def isValidPosition(self, cell_value: string, actual_elements: set) -> bool:
        if cell_value in actual_elements:
            return False

        actual_elements.add(cell_value)
        return True

    # calculates box to validate
    def getBox(self, row_position: int, col_position: int) -> int:
        return (row_position // 3) * 3 + (col_position // 3)
