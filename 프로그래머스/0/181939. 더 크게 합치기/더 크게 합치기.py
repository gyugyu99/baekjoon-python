def solution(a, b):
    A = str(a)+str(b) 
    B = str(b)+str(a)
    if int(A) != int(B):
        return int(max(A, B))
    else:
        return int(A)