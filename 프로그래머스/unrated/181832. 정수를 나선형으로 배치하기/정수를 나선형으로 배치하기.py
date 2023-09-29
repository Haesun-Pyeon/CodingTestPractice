def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    val = 1
    i = n
    j = 0
    
    while True:
        while y < i:
            answer[x][y] = val
            val += 1
            y += 1
        y -= 1
        x += 1
        while x < i:
            answer[x][y] = val
            val += 1
            x += 1
        x -= 1
        y -= 1
        while y >= j:
            answer[x][y] = val
            val += 1
            y -= 1
        y += 1
        x -= 1
        while x > j:
            answer[x][y] = val
            val += 1
            x -= 1
        x += 1
        y += 1
        if val > n**2 : break
        i -= 1
        j += 1
    return answer
