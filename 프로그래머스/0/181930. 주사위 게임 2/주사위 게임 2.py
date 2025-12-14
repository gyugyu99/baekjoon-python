def solution(a, b, c):
    numset = {a, b, c}
    if len(numset) == 3:
        return a + b + c
    elif len(numset) == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)