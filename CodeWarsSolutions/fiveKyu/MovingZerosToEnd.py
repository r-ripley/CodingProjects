def move_zeros(lst):
    orig = len(lst)
    arr = []
    for item in lst:
        if item != 0:
            arr.append(item)
    diff = len(lst) - len(arr)
    for i in range(diff):
        arr.append(0)
    return arr