import random
import re


class Board:
    def __init__(self, dim_size, num_bombs) -> None:
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        # create the board using helper function
        self.board = self.new_board()
        self.assign_values()

        # initilaize a set to keep track of uncovered locations this set will contain (row, col) tuples
        self.dug = set()

    def new_board(self):
        # construct a board based on the dim size and the num bombs
        # this will use a 2d array
        board = [[None for _ in range(self.dim_size)]
                 for _ in range(self.dim_size)]
        # plant the bombs
        bombs_planted = 0  # counter
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            # check if this location already has a bomb
            if board[row][col] == '*':
                continue  # dont plant a bomb
            # plant the bomb
            board[row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_neighboring_bombs(r, c)

    def get_neighboring_bombs(self, row, col):
        neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    neighboring_bombs += 1
        return neighboring_bombs

    def dig(self, row, col):
        # dig at location [row][col], returning true if dig is succsefull and return false if [row][col] is a bomb
        # dig senarios:
        # hit a bomb -> game over
        # dig a location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursivly dig the neighbors.

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        # if our initial dig did not hit a bomb we SHOULDN'T hit a bomb here
        return True

    def __str__(self) -> str:
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(
            self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len
        return string_rep


def play(dim_size=10, num_bombs=10):
    # 1. Create the board, and plant the bombs
    board = Board(dim_size, num_bombs)
    # 2. show the user the board, and ask them where they want to dig
    # 3a. if the position IS a bomb, game over
    # 3b. if the location IS NOT a bomb, dig recursivly until each square is at least next to a bomb
    # 4. repeat steps 3 and 4 until there are no more places to dig
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input('Where would you like to dig? Input as row,col: '))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row > board.dim_size or col < 0 or col > board.dim_size:
            print('Invalid location. Try again.')
            continue

        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print('Congratulations!!! YOU WON!!!')
        print(board)
    else:
        print('SOORRY YOU LOST! GAME OVER!!')
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == '__main__':
    play()
