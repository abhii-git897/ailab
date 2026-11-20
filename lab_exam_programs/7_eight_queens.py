n = 8
board = [-1] * n

def solve(row):
    if row == n:
        return True
    for col in range(n):
        safe = True
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                safe = False
        if safe:
            board[row] = col
            if solve(row + 1):
                return True
    return False

solve(0)

for i in range(n):
    for j in range(n):
        if board[i] == j:
            print("Q", end=" ")
        else:
            print("-", end=" ")
    print()
