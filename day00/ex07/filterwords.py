import sys

def filterwords(str, size):
    i = len(sys.argv)
    if i == 3:
        if size.isdigit() is True and str.isdigit() is False:
            lst2 = []
            lst = []
            lst = str.split(' ')
            for word in lst:
                word = word.replace(",", "")
                if len(word) > int(size):
                    lst2.append(word)
            print(lst2)
        else:
            print("ERROR")
    else:
        print("ERROR2")

filterwords(sys.argv[1], sys.argv[2])
