def solution(numbers, k):
    answer = 1 + 2*(k-1)
    if answer > len(numbers):
        answer = answer % len(numbers)
        if answer == 0:
            answer = len(numbers)
    return answer