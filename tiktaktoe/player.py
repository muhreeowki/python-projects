import random
import math

#Default player class
class Player:
    #Player constructor
    def __init__(self, letter):
        self.letter = letter

    #Base function
    #Each child of this class will define their own implimentation of this function.
    def get_move(self, game: object) -> int:
        pass 

#Computer player class. This is a child of the player class
class ComputerPlayer(Player):
    #Call the superclass constructor.
    def __init__(self, letter):
        super().__init__(letter)

    #Get move function for the computer player chooses a random spot from the available moves
    def get_move(self, game: object) -> int:
        # return a random spot in the available moves
        return random.choice(game.available_moves())

class HumanPlayer(Player):
    #Call the superclass constructor.
    def __init__(self, letter):
        super().__init__(letter)
    
    # Get move for the human player will prompt continuously prompt the user for a valid spot until one is provided
    # This will use a while loop
    def get_move(self, game: object) -> int:
        valid_square = False
        val = None
        while not valid_square:
            # prompt user for input
            square = input(f'It is {self.letter}\'s turn to play. input a valid move (0-9): ')
            try:
                # try convert the user input into a string. If error then it was not a valid input.
                val = int(square)
                # Check if the number is between 0 and 9 and that the number is in available moves
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game: object) -> int:
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #randomly choose a square
        else:
            # get square from minimax function 
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, game, player):
        max_player = self.letter #yourself
        other_player = 'O' if player == 'X' else 'X' #other player
        
        # first check for a winner
        # this is the base case for this function
        if game.current_winner == other_player:
            # return the position and the score.
            return {
                'position': None,
                'score': 1 * (game.num_empty_squares() + 1) if other_player == max_player else -1 * (game.num_empty_squares() + 1)
            }

        elif not game.empty_squares(): #no empty square
            return {
                'position': None,
                'score': 0
            }

        # Initialize some dictionaries
        if player == max_player:
            best = {
                'position': None,
                'score': -math.inf #maximize. get the highest value
            }
        else:
            best = {
                'position': None,
                'score': math.inf #minimize. get the lowest value
            }

        # main algorithm
        for possible_move in game.available_moves():
            # 1. make a move, try that possible_move
            game.move(possible_move, player)
            # 2. recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(game, other_player) #alternate players
            # 3. undo the move
            game.board[possible_move] = ' '
            game.current_winner = None
            sim_score['position'] = possible_move #set the position
            # 4. update the dictionaries if necessary
            if player == max_player:  # we are try to maximize the win of the max_player
                if sim_score['score'] > best['score']: 
                    best = sim_score # replace the best move
            else: # minimize the other player
                if sim_score['score'] < best['score']: 
                    best = sim_score # replace the best move

        
            # return the best possible position and the score it yields
        return best
