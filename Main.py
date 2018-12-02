# TicTac-Toe by JustHosi
# Copyright 2018


import random
# This function creats the board shape.


def display_bord(board):
    print('\n' * 100)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])


def display_sample_bord(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])


# This function picks sides between X or O.
def player_input():
    while True:
        player_1 = input('Player 1, Pleae select X or O\n')
        if player_1.upper() == 'X' or player_1.upper() == 'O':
            break
    player_1 = player_1.upper()
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return player_1, player_2


# Put X or O in board position
def place_marker(board, marker, position):
    board[position] = marker


# This function checks if someone won the game
def win_check(board, mark):
            # Check if rows are X or O
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            # check if colums are X or O
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            # chek if diagnals are X or O
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


# This indicates who's going to start first
def choose_first():
    first = random.randint(1, 2)
    print('Player', first, 'Starts the game:\n')
    return first


# this checks if a space in the board is free availble
def space_check(board, position):
    return board[position] == ' '


# This checks if board is complete
def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    else:
        return True


# Ask for players next position wants to play
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def reply():
    continue_exit = input('For reply press "r", for exit press "e"\n')
    return continue_exit.lower()


while True:
    print('Welcome to JustHosi Tic-Tac-Toe')

    run = True
    theBoard = [' ']*10
    sample_board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    board = [' ']*10
    player1_marker, player2_marker = player_input()
    if choose_first() == 1:
        turn = 1
    else:
        turn = 2

    while run:
        print('This is sample board.\nYou should follow this positions indicated by the numbers')
        display_sample_bord(sample_board)
        if turn == 1:
            print('Player 1 turn:')
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            display_bord(theBoard)
            if win_check(theBoard, player1_marker):
                print('Player 1 won!')
                run = False
            elif full_board_check(theBoard):
                print('Tie all')
                run = False
            else:
                turn = 2
        else:
            print('Player 2 turn:')
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            display_bord(theBoard)
            if win_check(theBoard, player2_marker):
                print('Player 2 won!')
                run = False
            elif full_board_check(theBoard):
                print('Tie all')
                run = False
            else:
                turn = 1
    if reply() != 'r':
        print('Thank you for playing this game! Hope to see you again')
        break
