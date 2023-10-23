def solution(code):
    mode = False
    ret = ''
    for i, c in enumerate(code):
        if c == '1':
            mode = True if mode == False else False
        elif not mode:
            if i % 2 == 0:
                ret += c
        else:
            if i % 2 != 0:
                ret += c
    if ret:
        return ret
    else:
        return "EMPTY"