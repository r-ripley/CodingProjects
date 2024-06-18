def is_valid_walk(walk):
    from collections import Counter
    if len(walk) > 10 or len(walk) < 10:
        return False
    directions = Counter(walk)
    # check if north and south are walked the same, as well as west and east
    if directions['n'] - directions['s'] == 0 and directions['w'] - directions['e'] == 0:
        return True
    else:
        return False