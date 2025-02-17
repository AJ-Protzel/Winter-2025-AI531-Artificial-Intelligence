# Consider the problem of putting "as many knights as possible" on the board without any attacks. Explain how to solve this with local search, by defining appropriate ACTIONS and RESULT functions and a sensible objective function.






import random

class Knights:
    def __init__(self, n):
        self.n = n
        self.knights = []

    def is_safe(self, row, col):
        for (r, c) in self.knights:
            if abs(r - row) == 2 and abs(c - col) == 1:
                return False
            if abs(r - row) == 1 and abs(c - col) == 2:
                return False
        return True

    def action(self, row, col):
        if self.is_safe(row, col):
            self.knights.append((row, col))
            return True
        return False

    def result(self):
        new_board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for (row, col) in self.knights:
            new_board[row][col] = 1
        return new_board

    def objective(self):
        return len(self.knights)

    def hill_climbing(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.action(row, col):
                    current_value = self.objective()
                    if current_value < len(self.knights):
                        self.knights.pop()
        return self.result()

# Example usage
n = 2
knights = Knights(n)
board = knights.hill_climbing()
print(board)
