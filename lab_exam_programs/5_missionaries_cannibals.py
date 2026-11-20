from collections import deque

q = deque([(3, 3, 1)])
visited = set()
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

while q:
    m, c, b = q.popleft()
    if (m, c, b) in visited:
        continue
    visited.add((m, c, b))
    print(m, c, b)
    if m == 0 and c == 0:
        print("Goal Reached")
        break
    for x, y in moves:
        if b == 1:
            a, d = m - x, c - y
            boat = 0
        else:
            a, d = m + x, c + y
            boat = 1
        if 0 <= a <= 3 and 0 <= d <= 3:
            if (a == 0 or a >= d) and (3 - a == 0 or 3 - a >= 3 - d):
                q.append((a, d, boat))
