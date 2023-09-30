def solution(s):
    answer = ''
    s = s.lower()
    if s[0].isalpha():
        answer += s[0].upper()
    else: answer += s[0]
    
    for i, char in enumerate(s[1:], start=1):
        if s[i-1] == " " and char.isalpha():
            char = char.upper()
        answer += char
    return answer