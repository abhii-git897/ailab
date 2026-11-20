def alphabeta(d, n, alpha, beta, maxplayer):
    if d == 2:
        return tree[n]
    if maxplayer:
        v = -999
        for i in range(2):
            v = max(v, alphabeta(d + 1, n * 2 + i, alpha, beta, False))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = 999
        for i in range(2):
            v = min(v, alphabeta(d + 1, n * 2 + i, alpha, beta, True))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

tree = [3, 5, 6, 9]
print("Best Value:", alphabeta(0, 0, -999, 999, True))
