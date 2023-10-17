def solution(quiz):
    answer = []
    for q in quiz:
        expr, result = q.split('=')
        if eval(expr) == int(result):
            answer.append("O")
        else:
            answer.append("X")
    return answer