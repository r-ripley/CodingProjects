def is_valid_IP(addy):
    if len(addy.split('.')) != 4:
        return False
    for octet in addy.split('.'):
        if octet.isnumeric():
            if int(octet) < 0 or int(octet) > 255 or (octet[0] == '0' and len(octet) > 1):
                return False
        else:
            return False
    return True