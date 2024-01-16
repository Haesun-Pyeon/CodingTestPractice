def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk) == 0 or stk[-1] != arr[i]:
            stk.append(arr[i])
        else :
            stk = stk[:-1]
    if len(stk) == 0:
        stk.append(-1)
    return stk