def solution(n):
    n1 = 1
    n2 = 1
    for i in range(1, n+1):
        if i == 1 or i == 2:
            answer = n2
        else:
            n1, n2 = n2, n1 + n2
            answer = n2
    return answer % 1234567