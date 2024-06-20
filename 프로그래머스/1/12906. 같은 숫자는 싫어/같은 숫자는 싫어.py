def solution(arr):
    answer = [-1]
    for a in arr:
        if a != answer[-1]:
            answer.append(a)
    answer.pop(0)
    return answer