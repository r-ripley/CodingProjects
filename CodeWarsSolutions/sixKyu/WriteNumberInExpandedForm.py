def expanded_form(num):
    s = str(num)
    size = len(s)
    expanded = ""
    for ch in s:
        if int(ch) != 0:
            expanded += f'{int(ch) * 10**(size-1)} + '
        size -= 1
    return expanded[:-3]