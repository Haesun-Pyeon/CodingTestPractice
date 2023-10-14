def solution(n):
    i, num = 0, 1
    while num < n:
        i += 1
        num *= i
    if num == 1:
        return num
    elif num == n:
        return i
    else:
        return i-1