def is_valid_walk(walk):
    from collections import Counter
    if len(walk) > 10 or len(walk) < 10:
        return False
    directions = Counter(walk)
    if directions['n'] - directions['s'] == 0 and directions['w'] - directions['e'] == 0:
        return True
    else:
        return False