import sys

x = len(sys.argv)

def usage():
    print("Usage: python operations.py <number1> <number2>\nExample:\n  python operations.py 10 3")

if x == 1:
    usage()
elif x == 3:
    if sys.argv[1].isdigit() is True and sys.argv[2].isdigit() is True:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = float(sys.argv[1])
        d = float(sys.argv[2])
        print("Sum:         ", (a + b))
        print("Difference:  ", (a - b))
        print("Product:     ", (a * b))
        if b != 0:
            print("Quotient:    ", (c / d))
            print("Remainder:   ", (a % b))
        else :
            print("Quotient:     ERROR (div by zero)")
            print("Remainder:    ERROR (modulo by zero)")
    else :
        print("InputError:  only numbers")
        usage()
elif x > 3:
    print("InputError:  too many arguments\n")
    usage()
else :
    usage()
