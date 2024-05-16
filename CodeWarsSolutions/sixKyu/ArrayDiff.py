def array_diff(a, b):
    diff = []
    for item in a:
        if item not in b:
            diff.append(item)
    return diff