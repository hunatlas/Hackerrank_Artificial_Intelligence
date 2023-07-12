#!/usr/bin/python

def next_move(posr, posc, board):
    c = min([(i, j) for i, row in enumerate(board) if 'd' in row for j, column in enumerate(row) if column == 'd'], key = lambda x: abs(posr - x[0]) + abs(posc - x[1]))
    print("RIGHT" if c[1] > posc else "LEFT" if c[1] < posc else "UP" if posr > c[0] else "DOWN" if posr < c[0] else "CLEAN")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
