"""
name: Fiona Cremins
desc: Rock, Paper, Scissors Game
"""

# Import random numbers
from random import randint

# Put a while loop in case of draw
player = True
while player is True:
    player = False

    computer = randint(1, 3)

    # Create a list
    choice = ['rock', 'paper', 'scissors']

    # Computers choice
    computers_choice = choice[computer-1]

    # Ask the user to enter choice
    user = input('Enter Rock, Paper or Scissors: ')

    # Print the computers choice
    print('Computer chose: ' , computers_choice)

    # if statements to show who won

    if user == computers_choice:
        print('You have drawn with the computer. Try Again.')
        player = True

    elif user == 'rock' and computers_choice == 'scissors':
        print('You win!')
    elif user == 'scissors' and computers_choice == 'rock':
        print('You Lose!')

    elif user == 'scissors' and computers_choice == 'paper':
        print('You win!')
    elif user == 'paper' and computers_choice == 'scissors':
        print('You Lose!')

    elif user == 'rock' and computers_choice == 'paper':
        print('You win! Play again?')
    elif user == 'paper' and computers_choice == 'rock':
        print('You Lose! Try Again.')

    else:
        print('Error')


