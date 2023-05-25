from player import HumanPlayer, ComputerPlayer, GeniusComputerPlayer
import time

class TikTakToe:
    def __init__(self):
        # Game needs a board and current winner.
        self.board = [' ' for _ in range(9)] # This is a list comprehension that puts 9 spaces in a list.
        self.current_winner = None #keep track of the winner

    # This function takes in self. It prints out self.board in a 3x3 grid layout
    # prints the following:
    # |  |  |  |
    # |  |  |  |
    # |  |  |  |
    # as the game goes one it prints the letters in the boxes
    def print_board(self) -> None:
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # This is a function that is not unique to the object, so it is a static method
    # This function prints out the board with the indexes.
    # prints the following:
    # | 0 | 1 | 2 |
    # | 3 | 4 | 5 |
    # | 6 | 7 | 8 |
    @staticmethod
    def print_board_nums() -> None:
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # Returns a list of indicies of the available spaces
    def available_moves(self) -> list:
        return [i for i, spot in enumerate(self.board) if spot == ' ']        
        # available_moves = []
        # for (square, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         available_moves.append(square)
    
    # Returns true or false depending if there are available moves.
    # this return statement returns true if there is a ' ' (space) in self.board
    # it also returns false if there is no space in self.board
    def empty_squares(self) -> bool:
       return ' ' in self.board
        
    # Returns the number of empty squares on the board
    def num_empty_squares(self) -> int:
        return self.board.count(' ') #this will count the number of spaces
        # this is an alternative to the return statement above :
        # return len(self.available_moves())
    
    # This function takes in a 'square' that is an index on the board. 
    # It also takes in the letter of the player.
    # If the square the player inputs is a valid square then the function places 'letter' at that index 'square'
    # Returns true if the move was made and false otherwise.
    def move(self, square: int, letter: str) -> bool:
        # Check if the move is valid. This is not extremely important because the get_move player method already validates the move.
        if self.board[square] == ' ':
            # Assign the letter to the square
            self.board[square] = letter
            # Chekc if there is a winner
            if self.winner(square, letter):
                # if there is a winner, set current winner var to be the letter of the player.
                self.current_winner = letter
            return True
        return False

    # Returns true or false if their is a winner.
    # True is defined when a player gets 3 in a row either horizontaly, verticaly or diagonaly
    def winner(self, square: int, letter: str) -> bool:
        # CHECK THE ROW
        # divide square by 3 and floor it to find the row it came from
        row_in = square // 3
        # define a row
        row = self.board[row_in*3 : (row_in + 1) * 3]
        # check if all items in the row are equal to the value of letter. eg xxx or ooo
        if all([spot == letter for spot in row]):
            return True
            
        # CHECK COLUMN
        # The index of the top of the column is equal to the remainder of square divided by 3
        col_in = square % 3
        # define a column
        column = [self.board[col_in+i*3] for i in range(3)]
        # check if all items in the row are equal to the value of letter. eg xxx or ooo
        if all([spot == letter for spot in column]):
            return True

        # CHECK DIAGONALS
        # Diagonals can only be on even numbers
        # these are the only possible combinations to win a diagonal
        # [0, 2, 4] and [4, 6, 8]
        # define and check the first diagonal
        diagonal_1 = [self.board[i] for i in [0, 4, 8]] # top left to bottom right diagonal
        if all([spot == letter for spot in diagonal_1]):
            return True
        # defin and check the second diagonal
        diagonal_2 = [self.board[i] for i in [2, 4, 6]] # top right to bottom left diagonal
        if all([spot == letter for spot in diagonal_2]):
            return True

        # If all the checks dont return then there is no winner and we return false 
        return False

# Main function of the game. 
# Takes in two player objects and a TikTakToe object.
# Takes a boolean value for weather or not the game should be displayed in the terminal 
# Iterate while the game still has empty squares
# We dont have to worry about the winner because this function will return when a winner is found
# which will break the loop
# This method wil return the winner of the game, if no winner then it will return a tie1
def play(game, x_player, o_player, print_game=True) -> str:
    if print_game:
        # Print the board with index numbers
        game.print_board_nums()
    # Define starting letter1
    letter = 'X'
    # Iterate while the game still has empty squares
    while game.empty_squares():
        # if the letter is x get a move from the x player
        if letter == 'X':
            square = x_player.get_move(game)
        # else get a move from the o player
        else:
            square = o_player.get_move(game)
        # pass the move and the letter to the game.move method.
        if game.move(square, letter):
            # display the information to the user, and print an updated board
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('') #prints empty line
            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')
                return letter
            # Next players turn, cycle between x and o
            letter = 'O' if letter == 'X' else 'X' # This is a ternary operator

        if print_game:
            time.sleep(1.0)

    # If the while loop condition is met and no winner was returned, it is a tie
    if print_game:
        print('Its a tie!')

# Start the game
if __name__ == '__main__':
    # Create a human player object for both X and O
    x_wins = 0
    o_wins = 0
    ties = 0
    for i in range(100):
        x_player = ComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        game = TikTakToe()
        result = play(game, x_player, o_player, False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'After 100 interations, we see that:\nX wins {x_wins} times\nO wins {o_wins} times\nAnd they tie {ties} times')
