def solution(n):
    count = 0
    start, end = 1, 1
    while start != n:
        if sum(range(start, end+1)) < n:
            end += 1
        else:
            if sum(range(start, end+1)) == n:
                count += 1
            start += 1
            end = start
    return count+1