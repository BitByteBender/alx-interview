#!/usr/bin/env python3
""" N Queens Problem - Interview question """


class NQueensSolver:
    """ Solves the N Queens Problem """
    def __init__(self, size):
        """ Constructor """
        self.size = size
        self.board = [-1] * size
        self.solutions = []

    def solve(self):
        """ Solves the N Queens prob and stores solution """
        self._place_queen(0)
        return self.solutions

    def _place_queen(self, row):
        """ Recursively tries too place a queen in ea row """
        if row == self.size:
            self.solutions.append(self._create_solution())
            return

        for c in range(self.size):
            if self._is_safe(row, c):
                self.board[row] = c
                self._place_queen(row + 1)
                self.board[row] = -1

    def _is_safe(self, row, col):
        """ Checks if placeing a queen at row & col is safe """
        for r in range(row):
            c = self.board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def _create_solution(self):
        """ Creates a solution from the current board state """
        return [[i, self.board[i]] for i in range(self.size)]


class NQueensCLI:
    """ Class responsible for user handling io """
    def run(self):
        """ Runs the CLI and handles io """
        try:
            size = self._validate_input()
            solver = NQueensSolver(size)
            solutions = solver.solve()
            for solution in solutions:
                print(solution)
        except ValueError as e:
            print(e)

    def _validate_input(self):
        """ Validates user input """
        usr_input = input("Enter the value of N (>=4): ").strip()

        try:
            size = int(usr_input)
        except ValueError:
            raise ValueError("N must be a number")

        if size < 4:
            raise ValueError("N must be at least 4")

        return size


if __name__ == "__main__":
    cli = NQueensCLI()
    cli.run()
