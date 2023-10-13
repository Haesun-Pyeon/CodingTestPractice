def solution(absolutes, signs):
    for i, sign in enumerate(signs):
        if not sign:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)