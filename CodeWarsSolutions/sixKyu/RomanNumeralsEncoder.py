def solution(n):
    numerals = ''
    values = [(1000,'M'),(900, 'CM'),
              (500, 'D'),(400, 'CD'),
              (100, 'C'),(90, 'XC'),
              (50, 'L'),(40, 'XL'),
              (10, 'X'),(9, 'IX'),
              (5, 'V'),(4, 'IV'),
              (1, 'I')]
    
    for item in values:
        while n >= item[0]:
            numerals += item[1]
            n -= item[0]
            
    return numerals