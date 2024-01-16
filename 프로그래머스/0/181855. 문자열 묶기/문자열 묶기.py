def solution(strArr):
    maxlen = 0
    for s in strArr:
        maxlen = max(maxlen, len(s))
    count = [0 for _ in range(maxlen)]
    for s in strArr:
        count[len(s)-1] += 1
    return max(count)