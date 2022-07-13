'''
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
'''

def conv(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

def add2(arg1, arg2):
    val1 = conv(arg1)
    val2 = conv(arg2)

    if isinstance(val1, str) or isinstance(val2, str):
        val1 = str(val1)
        val2 = str(val2)
    
    return val1 + val2
