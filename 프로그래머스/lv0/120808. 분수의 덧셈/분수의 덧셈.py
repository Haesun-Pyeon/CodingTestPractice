import math
def lcm(n1, n2):
    return (n1 * n2) // math.gcd(n1, n2)

def solution(numer1, denom1, numer2, denom2):
    denom_lcm = lcm(denom1, denom2)
    numer_sum = numer1 * (denom_lcm // denom1) + numer2 * (denom_lcm // denom2)
    answer = [numer_sum, denom_lcm]
    gcd = math.gcd(numer_sum, denom_lcm)
    if gcd != 1:
        numer_sum = numer_sum // gcd
        denom_lcm = denom_lcm // gcd
        answer = [numer_sum, denom_lcm]
    return answer