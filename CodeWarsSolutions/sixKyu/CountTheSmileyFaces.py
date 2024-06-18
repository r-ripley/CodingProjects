def count_smileys(arr):
    count = 0
    
    # iterate through array and count each possible smiley
    for item in arr:
        if len(item) == 2:
            if (item[0] == ':' or item[0] == ';') and (item[1] == ')' or item[1] == 'D'):
                count += 1
                
        elif len(item) == 3:
            if (item[0] == ':' or item[0] == ';') and (item[1] == '-' or item[1] == '~') and (item[2] == ')' or item[2] == 'D'):
                count += 1
            
    return count