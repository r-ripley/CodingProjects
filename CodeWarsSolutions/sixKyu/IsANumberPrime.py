def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**.5) + 1):
        if i % num == 0:
            return False
    return True