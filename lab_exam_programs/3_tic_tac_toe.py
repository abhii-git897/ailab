b = [" "] * 9

def show():
    print(b[0:3])
    print(b[3:6])
    print(b[6:9])

def check(p):
    w = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(b[x] == b[y] == b[z] == p for x, y, z in w)

while True:
    show()
    x = int(input("Enter position 0-8: "))
    if x < 0 or x > 8 or b[x] != " ":
        print("Invalid position")
        continue
    b[x] = "X"
    if check("X"):
        show()
        print("You Win")
        break
    if " " not in b:
        show()
        print("Draw")
        break
    
    best = -999
    move = -1
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            if check("O"):
                score = 1
            else:
                score = 0
            b[i] = " "
            if score > best:
                best = score
                move = i
                
    b[move] = "O"
    if check("O"):
        show()
        print("Computer Wins")
        break
    if " " not in b:
        show()
        print("Draw")
        break
