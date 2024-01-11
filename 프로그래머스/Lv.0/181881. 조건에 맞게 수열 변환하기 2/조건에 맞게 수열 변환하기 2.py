def solution(arr):
    answer, change = 0, 0
    while True:
        for i, a in enumerate(arr):
            if a >= 50 and a % 2 == 0:
                arr[i] = a // 2
                change += 1
            elif a < 50 and a % 2 != 0:
                arr[i] = 2 * a + 1
                change += 1
        if change == 0:
            return answer
        else:
            answer += 1
            change = 0