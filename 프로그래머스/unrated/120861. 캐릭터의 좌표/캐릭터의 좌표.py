def solution(keyinput, board):
    answer = [0, 0]
    width = (board[0] - 1) // 2
    height = (board[1] - 1) // 2
    for k in keyinput:
        if k == 'up':
            answer[1] += 1
            if answer[1] > height:
                answer[1] = height
        elif k == 'down':
            answer[1] -= 1
            if answer[1] < -height:
                answer[1] = -height
        elif k == 'right':
            answer[0] += 1
            if answer[0] > width:
                answer[0] = width
        elif k == 'left':
            answer[0] -= 1
            if answer[0] < -width:
                answer[0] = -width
    return answer