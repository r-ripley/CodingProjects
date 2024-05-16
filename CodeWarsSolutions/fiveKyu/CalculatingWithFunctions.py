def zero(func=None, *num): 
    return func(0, *num) if func else 0 

def one(func=None, *num): 
    return func(1, *num) if func else 1

def two(func=None, *num): 
    return func(2, *num) if func else 2

def three(func=None, *num): 
    return func(3, *num) if func else 3

def four(func=None, *num): 
    return func(4, *num) if func else 4

def five(func=None, *num): 
    return func(5, *num) if func else 5

def six(func=None, *num): 
    return func(6, *num) if func else 6

def seven(func=None, *num): 
    return func(7, *num) if func else 7

def eight(func=None, *num): 
    return func(8, *num) if func else 8

def nine(func=None, *num): 
    return func(9, *num) if func else 9

def plus(num): return lambda x: x + num
def minus(num): return lambda x: x - num
def times(num): return lambda x: x * num
def divided_by(num): return lambda x: x // num