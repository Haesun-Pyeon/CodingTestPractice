def solution(order):
    answer = 0
    for o in order:
        if 'latte' in o:
            answer += 5000
        else:
            answer += 4500
    return answer