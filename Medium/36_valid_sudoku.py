class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Sudoku Visualization
        #__________________________________________
        #|      |    (0)    |    (1)    |   (2)    |       
        #|      | 0   1   2 | 3   4   5 |6   7   8 |
        #|______|___________|___________|__________|
        #|    0 |           |           |          |
        #|(0) 1 |           |           |          |
        #|    2 |           |           |          |
        #|______|___________|___________|__________|
        #|    3 |           |           |          |
        #|(1) 4 |           |           |          |
        #|    5 |           |           |          |
        #|______|___________|___________|__________|
        #|    6 |           |           |          |
        #|(2) 7 |           |           |          |
        #|    8 |           |           |          |
        #|______|___________|___________|__________|
        #   - A sudoku can be a 3x3 grid of 3x3 boxes, that way, we can check each box (total 9 boxes) and see if it satisfy the condition
        #   - the box_key is a tuple of coordinate, where the position of the element determines which box it is at
        #   - where box_key = (box_row, box_col) = (row//3, col//3)
        #   - e.g. a (8, 0) would have a box_key of (2, 0)

        # Time complexity: O(n^2) for an n x n board, but since Sudoku is always 9x9, this is O(1)
        # Checking Sudoku will always be constant time, since the size is fixed and each loop is done seperately, instead of nested
        # We check rows, columns, and boxes separately (not nested), so efficiency is not a concern

        # Scan for repeating in each row
        for row in range(9):
            #Reset row sets to empty after every row scanned
            row_checked = set()

            # "col" is iterating here, means checking each element in a row
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if board[row][col] not in row_checked:
                    row_checked.add(board[row][col])
                else:
                    return False

        # Scan for repeating in each col
        for col in range(9):
            col_checked = set()

            # "row" is iterating here, means checking each element in a column
            for row in range(9):
                if board[row][col] == ".":
                    continue
                
                if board[row][col] not in col_checked:
                    col_checked.add(board[row][col])
                else:
                    return False

        # Imagine the 9x9 Sudoku board into a 3x3 grid with 9 boxes
        # A map is created for each 9 boxes, the key stores the position of where the element is when it becomes a 3x3 grid
        #   - position is a tuple, (x, y), where "x" is 0-2 and "y" is also 0-2
        #   - position is determined by (row//3, col//3), when it becomes a 3x3 grid
        boxes = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                box_key = (row // 3, col // 3)
                
                # if box_key is not in the map, create a new set and check for that box
                if box_key not in boxes:
                    boxes[box_key] = set()

                # for each iteration, if the element appears in the same box, where box is represented by box_key, returns false
                if board[row][col] in boxes[box_key]:
                    return False

                # add new elements to the value of the key each iteration
                boxes[box_key].add(board[row][col])

        return True
