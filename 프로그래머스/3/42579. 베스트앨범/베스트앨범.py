def solution(genres, plays):
    answer = []
    total = list(zip(genres, plays, range(len(genres))))
    total.sort(key=lambda x: (x[0], -x[1], x[2]))
    g_count = dict()
    for t in total:
        if t[0] not in g_count.keys():
            g_count[t[0]] = t[1]
        else:
            g_count[t[0]] += t[1]
    basis = list(map(lambda x: x[0], sorted(g_count.items(), key=lambda x: x[1], reverse=True)))
    print(basis)
    for b in basis:
        i = 0
        for t in total:
            if b == t[0] and i < 2:
                answer.append(t[2])
                i += 1
    return answer