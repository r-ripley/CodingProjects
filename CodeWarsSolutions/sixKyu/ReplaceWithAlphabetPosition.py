def alphabet_position(text):
    return ' '.join([str(ord(ch) - 96) for ch in text.lower().replace(' ', '') if ch.isalpha])