def solution(arr, n):
    answer = []
    if len(arr) % 2 != 0:
        for i, a in enumerate(arr):
            if i % 2 == 0:
                a += n
            answer.append(a)
    else:
        for i, a in enumerate(arr):
            if i % 2 != 0:
                a += n
            answer.append(a)
    return answer