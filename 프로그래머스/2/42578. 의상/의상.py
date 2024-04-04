from collections import Counter

def solution(clothes):
    category = list(map(lambda x: x[1], clothes))
    count = Counter(category)
    result = 1
    for c in count.values():
        result *= (c+1)
    return result - 1