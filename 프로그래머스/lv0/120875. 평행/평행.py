import math

def solution(dots):
    a, b, c, d = dots
    combs = [[[a, b], [c, d]], [[a, c], [b, d]], [[a, d], [b, c]]]
    gradients = ()
    for comb in combs:
        for c in comb:
            x = abs(c[0][0] - c[1][0])
            y = abs(c[0][1] - c[1][1])
            gcd = math.gcd(x, y)
            if gcd > 1:
                x = x // gcd
                y = y // gcd
            if not gradients:
                gradients = (x, y)
            elif (x, y) == gradients:
                return 1
            else:
                gradients = ()
    return 0