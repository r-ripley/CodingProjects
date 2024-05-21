def rot13(message):
    # uppercase: A-65, Z-90
    # lowercase: a-97, z-122
    translated = ""
    for ch in message:
        if ord(ch) >= 97 and ord(ch) <= 122:
            if ord(ch) + 13 >= 123:
                translated = translated + chr((ord(ch)-13))
            else:
                translated = translated + chr((ord(ch)+13))
                
        elif ord(ch) >= 65 and ord(ch) <= 90:
            if ord(ch) + 13 >= 91:
                translated = translated + chr((ord(ch)-13))
            else:
                translated = translated + chr((ord(ch)+13))
        else:
            translated = translated + ch
                
    return translated
