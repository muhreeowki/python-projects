# helper function that returns a tuple of the row, col of an empty position in the puzzle
def find_next_empty(puzzle): 
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c   
    return None, None

def is_valid(puzzle, guess, row, col):
    # helper function that checks if a guess is valid
    # returns true if is valid and false otherwise

    # check the row first
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
        
    # check the columns
    col_vals = [puzzle[1][col] for i in range(9)]
    if guess in col_vals:
        return False

    # check the 3x3 box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if function gets to this point the guess is valid
    return True



def solve_sudoku(puzzle):
    # puzzle is a 2d array
    # step 1: chosse somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: check if the find_next_empty helper function returned a position. if none then the game is over
    if row == None:
        return True

    # step 2: if a position was returned then make a guess
    for guess in range(1, 10): #try all the numbers between 1 and 9 inclusive.

        # step 3: if guess is valid, then place guess in our puzzle
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid OR our guess does not solve the puzzle, we need to back track
        puzzle[row][col] = -1

    # step 6: if the function gets here it means there was no solution meaning the board is unsolvable
    return False
    
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)

            
