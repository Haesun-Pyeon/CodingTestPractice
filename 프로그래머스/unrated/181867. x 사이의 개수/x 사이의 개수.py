def solution(myString):
    answer = []
    strs = myString.split('x')
    for s in strs:
        answer.append(len(s))
    return answer