def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0 and sosu(i):
            answer.append(i)
    return answer

def sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True