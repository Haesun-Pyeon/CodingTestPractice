def solution(s):
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if not stack:
        return 1
    else:
        return 0