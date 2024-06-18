def array_diff(a, b):
    # create a new list and add items from a if they are not in b
    diff = []
    for item in a:
        if item not in b:
            diff.append(item)
    return diff