def solution(my_string, s, e):
    answer = ''
    answer += my_string[:s]
    if s != 0:
        answer += my_string[e:s-1:-1]
    else:
        answer += my_string[e::-1]
    answer += my_string[e+1:]
    return answer