def solution(num):
    j = ""
    h = ""
    for i in num:
        if i % 2 == 0:
            j += str(i)
        else:
            h += str(i)
    return int(j) + int(h)