def solution(num_list):
    answer = 0
    for num in num_list:
        for i in range(6):
            if num < 2 ** i:
                answer += i - 1
                print(i-1)
                break
    return answer