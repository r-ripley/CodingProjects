def move_zeros(lst):
    orig = len(lst)
    # create a new list and add the item if not 0
    arr = []
    for item in lst:
        if item != 0:
            arr.append(item)
    # check how many zeroes you chopped off
    diff = len(lst) - len(arr)
    # add the zeroes back at the end
    for i in range(diff):
        arr.append(0)
    return arr