def max_sequence(arr):
    # track two seperate sums
    currentSum = 0
    maxSum = 0
    # add to sum and compare
    for x in arr:
        currentSum += x
        # if the new sum is higher than the current sum, replace it with current sum
        if currentSum > maxSum:
            maxSum = currentSum
        # if the sum is negative, reset to 0
        if currentSum < 0:
            currentSum = 0
    return maxSum