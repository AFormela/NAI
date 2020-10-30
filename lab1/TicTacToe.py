#Źródło problemu: https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
#Twórca rozwiązania: Aleksandra Formela, s17402

import sys
import math

def is_circle(board, row, column, choosenRow, choosenColumn):
    return board[row][column] == 'O' or (row == choosenRow and column == choosenColumn)

def check_row(board, row, choosenRow, choosenColumn):
    for column in range(3):
        if not is_circle(board, row, column, choosenRow, choosenColumn):
            return False
    return True

def check_rows(board, choosenRow, choosenColumn):
    for row in range(3):
        if check_row(board, row, choosenRow, choosenColumn):
            return True
    return False

def check_column(board, column, choosenRow, choosenColumn):
    for row in range(3):
        if not is_circle(board, row, column, choosenRow, choosenColumn):
            return False
    return True

def check_columns(board, choosenRow, choosenColumn):
    for column in range(3):
        if check_column(board, column, choosenRow, choosenColumn):
            return True
    return False

def check_right_diagonal(board, choosenRow, choosenColumn):
    for i in range(3):
        if not is_circle(board, i, i, choosenRow, choosenColumn):
            return False
    return True

def check_left_diagonal(board, choosenRow, choosenColumn):
    for i in range(3):
        if not is_circle(board, i, 2-i, choosenRow, choosenColumn):
            return False
    return True

def check_win(board, choosenRow, choosenColumn):
    return check_columns(board, choosenRow, choosenColumn) or check_rows(board, choosenRow, choosenColumn) or check_right_diagonal(board, choosenRow, choosenColumn) or check_left_diagonal(board, choosenRow, choosenColumn)


board = []
for i in range(3):
    line = input()
    board.append(line)

winX = -1
winY = -1
isWin = False
for i in range(3):
    for j in range(3):
        if board[i][j] == ".":
            if check_win(board, i, j):
                isWin = True
                winX = j
                winY = i

if not isWin:
    print("false")
else:
    resultBoard = []
    for i in range(3):
        resultBoard.append([])
        for j in range(3):
            if i == winY and j == winX:
                resultBoard[i].append('O')
            else:
                resultBoard[i].append(board[i][j])
    for i in range(3):
        print("".join(resultBoard[i]))
