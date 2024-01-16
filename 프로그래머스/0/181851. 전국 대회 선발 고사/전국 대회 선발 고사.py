def solution(rank, attendance):
    results = []
    for i in range(len(rank)):
        if attendance[i]:
            results.append([rank[i], i])
    results.sort()
    a, b, c = results[0][1], results[1][1], results[2][1]
    return 10000 * a + 100 * b + c