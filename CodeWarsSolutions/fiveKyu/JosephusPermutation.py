def permute(items, k) -> list:
    arr = []
    runs = len(items)
    spot = k - 1
    while items:
        while spot >= len(items):
            spot -= len(items)
        if len(items) == 1:
            arr.append(items[0])
            items.pop(0)
            break   
        arr.append(items[spot])
        items.pop(spot)
        spot += k-1

    return arr