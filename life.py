#
# life.py - Game of Life lab
#
# Name: Luke McEvoy
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys

def printBoard(A):
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def diagonalize(width,height):
    A = createBoard( width, height )
    
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
        return A


def innerCells(w,h):
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row < 1 or row == h-1:
                A[row][col] = 0
            elif col < 1 or col == w-1:
                A[row][col] = 0
            else:
                A[row][col] = 1

def randomCells(w,h):
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row < 1 or row == h-1:
                A[row][col] = 0
            elif col < 1 or col == w-1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])
    return A

def copy(A):
    B = createBoard(len(A), len(A[0]))
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[row][col] = A[row][col]
    return B

def innerReverse(A):
    B = createBoard(len(A), len(A[0]))
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row < 1 or row == len(A):
                B[row][col] = 0
            elif col < 1 or col == len(A[0]):
                B[row][col] = 0
            else:
                if A[row][col] == 0:
                    B[row][col] = 1
                else:
                    B[row][col] = 0
    return B


def next_life_generation(A):
    B = createBoard(len(A), len(A[0]))
    for row in range(len(A)-2):
        for col in range(len(A[0])-2):
            if A[row+1][col+1] == 1 and countNeighbors(row+1,col+1,A) < 2:
                B[row+1][col+1] = 0
            elif A[row+1][col+1] == 1 and countNeighbors(row+1,col+1,A) > 3:
                B[row+1][col+1] = 0
            elif A[row+1][col+1] == 0 and countNeighbors(row+1,col+1,A) == 3:
                B[row+1][col+1] = 1
            else:
                B[row+1][col+1] = A[row+1][col+1]
    return B

'''
All edge cells stay 0 
A cell that has fewer than two live neighbors dies
A cell that has more than 3 live neighbors dies
A cell that is dead and has exactly 3 live neighbors comes to life
All other cells maintain their state

analyze table1 and actions are on table 2

helper that finds the 8 neighbors and sees if they are alive

def helper(row, col, A):
    #A[row][col]
    for row in range(len(A)):
        for col in range(len(A[0])):
            Y = [ A[row+1][col-1] + \
            A[row+1][col+1] + \
            A[row-1][col-1] + \
            A[row-1][col+1] + \
            A[row][col-1] + \
            A[row][col+1] + \
            A[row-1][col] + \
            A[row+1][col] ]
        return Y

'''

def helper(row, col, A):
        print(A[row+1][col-1])
        print(A[row+1][col+1])
        print(A[row+1][col])
        print(A[row-1][col-1])
        print(A[row-1][col+1])
        print(A[row-1][col])
        print(A[row][col-1])
        print(A[row][col+1])
    
def countNeighbors(row, col, A):
    if row and col > 0:
        Y = \
        (A[row+1][col-1] + \
        A[row+1][col+1] + \
        A[row+1][col] + \
        A[row-1][col-1] + \
        A[row-1][col+1] + \
        A[row-1][col] + \
        A[row][col-1] + \
        A[row][col+1])
        return Y
    else:
        return 0








    
