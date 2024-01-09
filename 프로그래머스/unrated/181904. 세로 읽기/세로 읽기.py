def solution(my_string, m, c):
    answer = ''
    arr = []
    for i in range(len(my_string) // m):
        arr.append(my_string[i*m:i*m+m])
    for a in arr:
        answer += a[c-1]
    return answer