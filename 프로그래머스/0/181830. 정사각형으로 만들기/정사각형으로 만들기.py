def solution(arr):
    row = len(arr)
    column = len(arr[0])
    if row > column:
        for a in arr:
            a += [0] * (row - column)
    elif row < column:
        arr += [[0] * column] * (column - row)
    return arr