import random

p = [random.randint(1, 10) for i in range(5)]

for i in range(5):
    p.sort(reverse=True)
    print("Generation:", p)
    a = p[0]
    b = p[1]
    child = (a + b) // 2
    p[-1] = child

print("Best Solution:", max(p))
