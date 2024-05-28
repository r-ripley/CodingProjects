def title_case(title, minor_words=''):
    return title.split(' ')[0].capitalize() + ''.join(' ' + word.capitalize() if word.lower() not in minor_words.lower().split(' ') else ' ' + word.lower() for word in title.split(' ')[1:])