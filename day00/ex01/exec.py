import sys

def revert(str):
    return str[::-1].swapcase()

x = len(sys.argv) - 1

while x > 1:
    print(revert(sys.argv[x]), end=' ')
    x -= 1

print(revert(sys.argv[x]))
