'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argnumbers == 2:
    print("")
    sum = calc.add2(str(sys.argv[1]), str(sys.argv[2]))
    print("The result is " + str(sum))
    print("")
    sys.exit(0)

if argnumbers != 2:
    print("")
    print("You entered " + str(argnumbers) + "value/s.")
    print("")
    sys.exit(1)
