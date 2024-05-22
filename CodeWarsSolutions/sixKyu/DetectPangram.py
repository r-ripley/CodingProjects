def is_pangram(s):
    bank = []
    master = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for ch in s:
        if ch.isalpha() and ch.lower() not in bank and not ch.isdigit():
            bank.append(ch.lower())
    bank.sort()
    if bank == master:
        return True
    else:
        return False