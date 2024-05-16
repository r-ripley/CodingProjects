def likes(names):
    if names == []:
        return 'no one likes this'
    elif len(names) == 1:
        return names[0] + ' likes this'
    elif len(names) == 3:
        return names[0] + ', ' + " and ".join(names[-2:]) + " like this"
    elif len(names) >= 4:
        return ', '.join(names[:2]) + " and " + str(len(names)-2) + ' others like this'
    else:
        return ' and '.join(names[-2:]) + ' like this'