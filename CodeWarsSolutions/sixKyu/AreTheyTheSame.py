def comp(array1, array2):
    # check if the arrays are empty and not the same, then sort
    if array1 != None and array2 != None and len(array1) == len(array2):  
        array1 = sorted(array1, key = abs)
        array2.sort()
        # check each item in array
        for i in range(len(array1)):
            if array1[i]*array1[i] != array2[i]:
                return False
        return True
    else:
        return False