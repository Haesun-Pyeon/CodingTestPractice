def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        c = common[1] - common[0]
        answer = common[-1] + c
    elif common[1] / common[0] == common[2] / common[1]:
        c = common[1] / common[0]
        answer = int(common[-1] * c)
    return answer