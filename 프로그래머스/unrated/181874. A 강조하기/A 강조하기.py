def solution(myString):
    answer = ''
    for string in myString:
        if string in ('a', 'A'):
            answer += string.upper()
        else:
            answer += string.lower()
    return answer