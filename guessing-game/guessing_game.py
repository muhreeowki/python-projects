import random

def guess(n):
    random_number = random.randint(1, n)
    while True:
        user_guess = int(input(f"Guess a number between 1 and {n}: ").lower())
        if user_guess == random_number:  
            print(f'{user_guess} is correct!')
            break
        elif user_guess > random_number:
            print(f'{user_guess} is too High!')
        else:
            print(f'{user_guess} is too Low!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low == high:
            guess = high
        else: 
            guess = random.randint(low, high)
        
        feedback = input(f'Is {guess} too high (h), too low (l), or correct (c)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yess I guessed your number, {guess}, correctly!')


computer_guess(10)
