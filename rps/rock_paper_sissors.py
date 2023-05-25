import random

def play():
    rps = ['r', 'p', 's'] 
    user = input('Choose Rock (r), Paper(p), or Scissors(s): ').lower().strip()
    computer = random.choice(rps)
    # draw condition
    if user == computer:
        return(f'Computer chose: {computer} Its a tie!')

    # win condition
    if is_win(user, computer):
        return(f'Computer chose: {computer} You win!')

    #if not draw or win the loss
    return(f'Computer chose: {computer} You lose!')

# helper fucntion
def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True

    return False


play()