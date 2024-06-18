def high(x):
    # create a dictionary and add each word to it paired with their values according to ascii
    values = {}
    for word in x.split(" "):
        total = 0
        for ch in word:
            total += ord(ch) - 96
            values[word] = total
    return max(values, key=values.get)