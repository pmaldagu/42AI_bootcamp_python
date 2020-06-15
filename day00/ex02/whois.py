import sys

def whois(str):
    if (len(str) == 1):
        return 0
    elif (len(str) > 2 or str[1].isnumeric() is False):
        print("ERROR")
        return 0
    i = int(str[1])
    if (i == 0):
        print("I'm Zerro")
    elif (i % 2 == 0):
        print("I'm Even.")
    elif (i % 2 == 1):
        print("I'm Odd.")

whois(sys.argv)
