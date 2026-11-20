start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

while start != goal:
    print(start)
    z = start.index(0)
    if z + 3 < 9:
        start[z], start[z + 3] = start[z + 3], start[z]
    elif z + 1 < 9:
        start[z], start[z + 1] = start[z + 1], start[z]

print("Puzzle Solved")
print(goal)
