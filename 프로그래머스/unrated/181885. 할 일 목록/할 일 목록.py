def solution(todo_list, finished):
    result = []
    for todo, fin in zip(todo_list, finished):
        if not fin:
            result.append(todo)
    return result