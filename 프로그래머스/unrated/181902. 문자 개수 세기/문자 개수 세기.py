def solution(my_string):
    answer = [0 for _ in range(52)]
    for s in my_string:
        if s.isupper():
            idx = ord(s) - 65
        else:
            idx = ord(s) - 71
        answer[idx] += 1
    return answer