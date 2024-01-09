from collections import Counter

def solution(a, b, c, d):
    ints = [a, b, c, d]
    counts = Counter(ints)
    count = counts.most_common()
    if count[0][1] == 4:
        return 1111 * count[0][0]
    elif count[0][1] == 3:
        p = count[0][0]
        q = count[1][0]
        return (10 * p + q) ** 2
    elif count[0][1] == 2:
        if count[1][1] == 2:
            p = count[0][0]
            q = count[1][0]
            return (p + q) * abs(p - q)
        else:
            return count[1][0] * count[2][0]
    else:
        return min(ints)