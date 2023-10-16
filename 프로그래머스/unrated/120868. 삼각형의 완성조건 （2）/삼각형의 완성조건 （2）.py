def solution(sides):
    last_len = []
    max_len = sides[0] + sides[1] - 1
    min_len = abs(sides[0] - sides[1]) + 1
    for i in range(max(sides), max_len+1):
        if i not in last_len:
            last_len.append(i)
    for i in range(min_len, max(sides)+1):
        if i not in last_len:
            last_len.append(i)
    return len(last_len)