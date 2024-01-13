def solution(myStr):
    answer = []
    val = ''
    for s in myStr:
        if s == 'a' or s == 'b' or s == 'c':
            if val != '':
                answer.append(val)
                val = ''
        else:
            val += s
    answer.append(val)
    if answer == [""]:
        answer = ["EMPTY"]
    return answer