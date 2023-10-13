def solution(s):
    count_0 = 0
    count_trans = 0
    while s != '1':
        after = list(filter(lambda x: x == '1', s))
        count_0 += len(s) - len(after)
        count_trans += 1
        s = str(bin(len(after))[2:])
    return [count_trans, count_0]