def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ").split()
    fixed = ""
    for i in range(len(text)):
        if i != 0:
            fixed += text[i].capitalize()
        else:
            fixed += text[i]
    return fixed