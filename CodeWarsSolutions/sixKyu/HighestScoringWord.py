def high(x):
    values = {}
    for word in x.split(" "):
        total = 0
        for ch in word:
            total += ord(ch) - 96
            values[word] = total
    return max(values, key=values.get)