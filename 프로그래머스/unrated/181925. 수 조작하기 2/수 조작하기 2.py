def solution(numLog):
    answer = ''
    for i, num in enumerate(numLog):
        if i != 0:
            change = num - prev
            if change == 1:
                answer += 'w'
            elif change == -1:
                answer += 's'
            elif change == 10:
                answer += 'd'
            elif change == -10:
                answer += 'a'
        prev = num
    return answer