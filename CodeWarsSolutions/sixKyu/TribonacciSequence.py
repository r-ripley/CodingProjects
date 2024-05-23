def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < len(signature):
        return signature[:n]
    else:
        for i in range(n-3):
            signature.append(sum(signature[i:]))
        return signature