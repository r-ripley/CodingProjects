# initial solution
""" 
def hex_string_to_RGB(hex_string):
    r, g, b = int(hex_string[1:3], 16), int(hex_string[3:5], 16), int(hex_string[5:], 16)
    dict = {}
    dict['r'], dict['g'], dict['b']= r, g, b
    
    return dict
"""

# condensed solution, not sure if this looks easier to read at first glance
def hex_string_to_RGB(hex_string):
     
    return {'r': int(hex_string[1:3], 16), 'g': int(hex_string[3:5], 16), 'b': int(hex_string[5:], 16)}