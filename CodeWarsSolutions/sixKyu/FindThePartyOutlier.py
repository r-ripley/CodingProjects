def find_outlier(integers):
    evenCount = 0
    oddCount = 0
    evenLast = 0
    oddLast = 0
    for i in integers:
        if i % 2 == 0:
            evenCount = evenCount + 1
            evenLast = i
        if i % 2 != 0:
            oddCount = oddCount + 1
            oddLast = i
    if evenCount > oddCount:
        return oddLast
    else:
        return evenLast