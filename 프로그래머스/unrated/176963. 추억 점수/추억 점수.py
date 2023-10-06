def solution(name, yearning, photo):
    answer = []
    scores = {k: v for k, v in zip(name, yearning)}
    for p in photo:
        score = 0
        for name in p:
            if name in scores.keys():
                score += scores[name]
        answer.append(score)
    return answer