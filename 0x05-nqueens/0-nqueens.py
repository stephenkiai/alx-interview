#!/usr/bin/env python3
"""
N Queens puzzle
"""

import sys


class NQueensSolver:
    """Class for solving the N Queens problem."""
    def __init__(self, N):
        """Initialize the NQueensSolver with the board size N."""
        self.N = N
        self.board = [-1] * N

    def is_safe(self, row, col):
        """Check if it's safe to place a queen at board[row][col]"""
        for i in range(row):
            if (
                self.board[i] == col
                or self.board[i] - i == col - row
                or self.board[i] + i == col + row
            ):
                return False
        return True

    def print_solution(self):
        """Print the N Queens solution"""
        print([[i, self.board[i]] for i in range(len(self.board))])

    def solve_queens(self, row):
        """Recursively solve N Queens problem"""
        if row == self.N:
            self.print_solution()
            return

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_queens(row + 1)


def main():
    """
     Main function to handle command-line arguments
     and initiate the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(N)
    solver.solve_queens(0)


if __name__ == "__main__":
    main()
