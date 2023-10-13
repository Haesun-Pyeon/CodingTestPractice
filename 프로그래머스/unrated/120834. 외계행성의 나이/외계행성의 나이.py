def solution(age):
    answer = ''
    trans = [i for i in 'abcdefghij']
    for s in str(age):
        answer += trans[int(s)]
    return answer