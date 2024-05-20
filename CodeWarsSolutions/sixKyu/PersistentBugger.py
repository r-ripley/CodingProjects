def persistence(n):
    count = 0
    
    while n >= 10:
        base = 1
        for digit in str(n):
            base *= int(digit)
        count += 1
        n = base
    return count