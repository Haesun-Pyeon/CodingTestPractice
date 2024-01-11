def solution(arr, queries):
    for query in queries:
        a, b = query
        for i in range(a, b+1):
            arr[i] += 1
    return arr