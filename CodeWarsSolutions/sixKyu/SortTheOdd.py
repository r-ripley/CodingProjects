def sort_array(source_array):
    sortedArr = []
    for item in source_array:
        if item % 2 != 0:
            sortedArr.append(item)
    sortedArr.sort()
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            sortedArr.insert(i, source_array[i])
    return sortedArr