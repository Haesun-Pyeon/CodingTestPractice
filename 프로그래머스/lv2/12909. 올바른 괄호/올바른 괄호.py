def solution(s):
    open = []
    for char in s:
        if char == '(':
            open.append(char)
        else:
            if open:
                open.pop()
            else:
                return False
    if open:
        return False
    return True