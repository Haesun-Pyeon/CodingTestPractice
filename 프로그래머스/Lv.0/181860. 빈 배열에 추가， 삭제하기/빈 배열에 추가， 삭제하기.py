def solution(arr, flag):
    answer = []
    for i, f in enumerate(flag):
        if f:
            for j in range(2 * arr[i]):
                answer.append(arr[i])
        else:
            answer = answer[:-arr[i]]
    return answer