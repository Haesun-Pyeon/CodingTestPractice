def solution(picture, k):
    answer = []
    for p in picture:
        line = ''
        for char in p:
            line += char * k
        answer += [line] * k
    return answer