def max_sequence(arr):
    currentSum = 0
    maxSum = 0
    for x in arr:
        currentSum += x
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum