__author__ = 'Olav Espenes'
__email__ = 'olaves@nmbu.no'


from random import randint


def your_guess():
    input_guess = 0
    while input_guess < 1:
        input_guess = int(input('Your guess: '))
    return input_guess


def two_dices_throw():
    return randint(1, 6) + randint(1, 6)


"""Throwes two dices and add those together"""


def guess_a_throw(throw, guess):
    return throw == guess


"""Check if your throw are equal to your guess"""

if __name__ == '__main__':
    false_check = False
    attempts = 3
    throw = two_dices_throw()
    while not false_check and attempts > 0:
        guess = your_guess()
        false_check = guess_a_throw(throw, guess)
        if not false_check:
            print('Wrong, try again!')
            attempts -= 1
    if attempts > 0:
        print('You won {} points.'.format(attempts))
    else:
        print('You lost. Correct answer: {}'.format(throw))
