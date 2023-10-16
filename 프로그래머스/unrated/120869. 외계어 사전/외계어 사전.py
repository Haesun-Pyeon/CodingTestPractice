from itertools import permutations
def solution(spell, dic):
    permus = permutations(spell, len(spell))
    for p in permus:
        word = ''.join(p)
        if word in dic:
            return 1
    return 2