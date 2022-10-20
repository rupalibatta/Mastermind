"""
Student name: Rupali Batta
Date: 10/7/22

This program plays a game of mastermind against the user. 
The computer generates a hidden sequence of four colors and the user has to guess both color and position."""

import random

# Function definitions each with valid """...""" docstrings (use # only for inline comments) under the function header. 
# Functions should be separated by two blank lines each.


def make_random_code ():
    """
    Makes a random 4 letter string from 6 possible letters

    Parameters:
        none

    Returns:
        4 letter string
    """
    ans = ''
    for i in range (4):
        ans += random.choice(['R','G','B','Y','O','W'])
    return ans

def count_exact_matches (str1, str2):
    """
    Gives the number of places where two strings have the same letters in the same places

    Parameters:
        Two strings of equal length

    Returns:
        Count of the matching letters
    """
    same = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            same += 1
    return same

def count_letter_matches (str1, str2):
    '''
    Returns the amount of letters of two strings that are the same, independent of their order

    Parameters:
        Two strings of equal length

    Returns:
        Count of the same letters in both strings
    '''
    list1 = []
    list2 = []
    list1[:0] = str1
    list2[:0] = str2
    same = 0
    for i in list1: #RORO
        if i in list2:
            same += 1
            list2.remove(i)
    return same

def compare_codes (code, guess):
    '''
    Given a code and the user's guess, output the clue for how many colors they got correct and in the right order

    Parameters:
        The correct code and the user's guess, both strings of length 4

    Returns:
        A 4 character string made of b, w, and -'s. 
        b = right color, right position
        w = right color, wrong position
        - = wrong color
    '''
    count_black = count_exact_matches (code, guess)
    count_white = count_letter_matches (code, guess) - count_black
    count_blank = 4 - (count_black + count_white)
    return (count_black*'b' + count_white*'w' + count_blank*'-')

def run_game ():
    '''
    Combine all previous functions into a full game

    Parameters:
        n/a

    Returns:
        n/a, but prints prompts and results
    '''
    print ('New game.')
    code = make_random_code()
    result = ''
    moves = 0
    while not (result == 'bbbb'):
        guess = input ('Enter your guess:')
        result =  compare_codes (code, guess)
        print ('Result: ' + result)
        moves += 1
    print ('Congratulations! You cracked the code in ' + str(moves) + ' moves!')


if __name__ == '__main__':
    run_game()