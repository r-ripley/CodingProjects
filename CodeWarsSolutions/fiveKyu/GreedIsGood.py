def score(dice):
    from collections import Counter
    
    total = 0
    tally = Counter(dice)
    
    for item in tally.keys():
        while tally[item] >= 3:
            if item == 1:
                total += 1000
            else:
                total += item * 100
            tally[item]-=3
            
        if item == 1:
            total += tally[item] * 100
        elif item == 5:
            total += tally[item] * 50
            
    return total