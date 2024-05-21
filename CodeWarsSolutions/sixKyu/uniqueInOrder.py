def unique_in_order(sequence):
    stored = None
    cleansed = []
    for item in sequence:
        if item != stored:
            cleansed.append(item)
            stored = item

    return cleansed