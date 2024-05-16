def two_sum(numbers, target):
    for x in numbers:
        for y in numbers[1:]:
            if numbers.index(x) != numbers.index(y, 1) and x + y == target:
                return (numbers.index(x), numbers.index(y, 1))