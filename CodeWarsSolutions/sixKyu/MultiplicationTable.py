def multiplication_table(size):
    table = []
    for i in range(size):
        inner = []
        for j in range(size):
            inner.append((i+1)*(j+1))
        table.append(inner)
    return table