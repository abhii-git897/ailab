from collections import deque

q = deque([(0, 0)])
visited = set()

while q:
    x, y = q.popleft()
    if (x, y) in visited:
        continue
    visited.add((x, y))
    print(x, y)
    if x == 2 or y == 2:
        print("Target Reached")
        break
    q.extend([
        (4, y), (x, 3),
        (0, y), (x, 0),
        (x - min(x, 3 - y), y + min(x, 3 - y)),
        (x + min(y, 4 - x), y - min(y, 4 - x))
    ])
