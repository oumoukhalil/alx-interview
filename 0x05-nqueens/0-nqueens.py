#!/usr/bin/python3

from sys import argv, exit
from typing import List


def validator(args: List) -> None:
    """validator to check if the argument is valid

    Parameters
    ----------
    args: List
    list of arguments passed

    Return
    ------
    None
    """
    _len = len(args)
    if _len != 2:
        print("Usage: nqueens N")
        exit(1)
    else:
        try:
            N = int(args[1])
            if N < 4:
                print("N must be at least 4")
                exit(1)

        except ValueError:
            print("N must be a number")
            exit(1)


def is_safe(board: List, row: int, col: int) -> bool:
    """safety checking

    Arguments
    ---------
    board: List
    row: int
    col: int

    Return
    ------
    bool
    """
    for i in range(row):
        if (board[i] == col or board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def nqueens(board: List, row: int, N: int) -> None:
    """nqueen proble solve

    Arguments
    ---------
    board: List
    row: int
    N: int

    Return
    ------
    None
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            nqueens(board, row + 1, N)


def main():
    """ Entry - point"""
    try:
        validator(argv)
        N = int(argv[1])
        board = [-1] * N
        nqueens(board, 0, N)
    except SystemExit as e:
        exit(e.code)


if __name__ == "__main__":
    main()
