def solution(a, d, included):
    n = len(included)
    c = 0
    for i in range(n):
        if included[i]:
            c += a + i * d
        else:
            pass
    return c
        