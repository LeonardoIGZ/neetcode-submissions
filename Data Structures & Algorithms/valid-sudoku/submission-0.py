class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # 1. vertical search O(n^2)
        for j in range(cols):
            elements_col = set()
            for i in range(rows):
                if board[i][j] != '.' :
                    if board[i][j] in elements_col:
                        # is an invalid sudoku!
                        return False
                    elements_col.add(board[i][j])
        
        # 2 hortizontal search O(n^2)
        for i in range(rows):
            elements_row = set()
            for j in range(cols):
                if board[i][j] != '.' :
                    if board[i][j] in elements_row:
                        # is an invalid sudoku!
                        return False
                    elements_row.add(board[i][j])

        # 3. quadrant search O(n^2)
        sudoku_b = [set() for _ in range(9)]
        for i in range(rows):
            quadrant = 0
            for j in range(cols):
                if board[i][j] != '.' :
                    if i < 3 and j < 3:
                        quadrant = 0 
                    elif i < 3 and j < 6:
                        quadrant = 3
                    elif i < 3 and j < 9:
                        quadrant = 6
                    elif i < 6 and j < 3:
                        quadrant = 1
                    elif i < 6 and j < 6:
                        quadrant = 4
                    elif i < 6 and j < 9:
                        quadrant = 7
                    elif i < 9 and j < 3:
                        quadrant = 2
                    elif i < 9 and j < 6:
                        quadrant = 5
                    elif i < 9 and j < 9:
                        quadrant = 8

                    if board[i][j] in sudoku_b[quadrant]:
                        return False
                    sudoku_b[quadrant].add(board[i][j])
        return True            
