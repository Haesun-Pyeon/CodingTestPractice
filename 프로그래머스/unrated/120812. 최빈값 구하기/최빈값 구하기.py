from collections import Counter
def solution(array):
    common = Counter(array).most_common()
    print(common)
    if len(common) >= 2 and common[0][1] == common[1][1]:
        return -1
    else:
        return common[0][0]