from time import time

def generator(text, sep=" ", option=None):
    lst_option = ["shuffle", "unique", "ordered", None]
    if type(text) is not str or option not in lst_option:
        return "ERRROR"
    lst_word = text.split(sep)
    if option == "ordered":
        lst_word.sort(key=lambda x:(not x.islower(), x))
    elif option == "unique":
        lst_word = sorted(set(lst_word))
    elif option == "shuffle":
        while len(lst_txt) > 0:
            lst2.append(lst.pop(int(time()) % len(lst_txt) - 1))
            lst_txt = lst2
    return (lst_word)
    #while i < len(lst_word):

