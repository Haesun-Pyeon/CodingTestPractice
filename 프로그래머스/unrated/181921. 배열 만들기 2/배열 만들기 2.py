def solution(l, r):
    answer = []
    for i in range(l, r+1):
        j = str(i).replace('5','').replace('0','')
        if not j:
            answer.append(i)
    return answer if answer else [-1]