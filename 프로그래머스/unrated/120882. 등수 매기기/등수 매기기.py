def solution(score):
    avg = {}
    for i, s in enumerate(score):
        avg[i] = (s[0]+s[1])/2
    sort_avg = list(avg.keys())
    sort_avg.sort(key=lambda x: avg[x], reverse=True)
    
    print(avg)
    print(sort_avg)
    answer = [0 for _ in range(len(sort_avg))]
    rank = 0
    acc = 0
    prev = 0
    for idx in sort_avg:
        if idx != 0 and avg[prev] == avg[idx]:
            answer[idx] = rank
            acc += 1
        else:
            rank += (acc + 1)
            acc = 0
            answer[idx] = rank
        prev = idx
    print(answer)
    return answer