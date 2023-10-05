def solution(players, callings):
    rank = {}
    for i, v in enumerate(players):
        rank[v] = i
    for call in callings:
        idx = rank[call]
        rank[call] -= 1
        other = players[idx-1]
        rank[other] += 1
        players[rank[call]] = call
        players[rank[other]] = other
    return players