def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
        if len(answer) == k:
            break
    while True:
        if len(answer) < k:
            answer.append(-1)
        else:
            break
    return answer