def solution(n):
    result = 0
    if n % 2 != 0: #n이 홀수일때
        for i in range(0, n+1):
            if i % 2 != 0:
                result += i
        return result
    if n % 2 == 0: #n이 짝수일때
        for i in range(0, n+1):
            if i % 2 == 0:
                result += i ** 2
        return result