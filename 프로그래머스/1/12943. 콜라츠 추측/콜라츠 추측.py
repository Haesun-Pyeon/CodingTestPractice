def solution(num):
    count = 0
    for _ in range(500):
        if num == 1:
            return count
        elif num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = num * 3 + 1
        count += 1
    return -1