def solution(lines):
    
    onetwo = [max(lines[0][0], lines[1][0]), min(lines[0][1], lines[1][1])]
    twothree = [max(lines[1][0], lines[2][0]), min(lines[1][1], lines[2][1])]
    onethree = [max(lines[0][0], lines[2][0]), min(lines[0][1], lines[2][1])]
    
    overlap = []
    for line in [onetwo, twothree, onethree]:
        if line[0] < line[1]:
            overlap.append(line)
    print(overlap) #
    if len(overlap) == 0:
        return 0
    elif len(overlap) == 1:
        return overlap[0][1] - overlap[0][0]
    elif len(overlap) == 2:
        if overlap[0][1] < overlap[1][0] or overlap[1][1] < overlap[0][0]:
            return (overlap[0][1] - overlap[0][0]) + (overlap[1][1] - overlap[1][0])
        else:
            return max(overlap[0][1],overlap[1][1]) - min(overlap[0][0], overlap[1][0])
    else:
        if overlap[0][1] < overlap[1][0] and overlap[1][1] < overlap[2][0]:
            return (overlap[0][1] - overlap[0][0]) + (overlap[1][1] - overlap[1][0]) + (overlap[2][1] - overlap[2][0])
        else:
            overlap2 = []
            start, end = 100, -100
            for ov in overlap:
                start = min(start, ov[0])
                end = max(end, ov[1])
            return end-start
            
        