def wave(people):
    ocean = []
    people.lower()
    
    for i in range(len(people)):
        if people[i] != " ":
            letter = people[i]
            letter = letter.upper()
            joined = people[:i] + letter + people[i+1:]
            ocean.append(joined)
        
    return ocean