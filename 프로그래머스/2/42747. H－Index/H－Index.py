def solution(citations):
    for i in range(len(citations), 0, -1):
        count = 0
        for c in citations:
            if i <= c:
                count += 1
        if i <= count:
            return i    
    return 0