def solution(myString):
    answer = []
    myString = myString.split('x')
    for s in myString:
        if s != "":
            answer.append(s)
    answer.sort()
    return answer