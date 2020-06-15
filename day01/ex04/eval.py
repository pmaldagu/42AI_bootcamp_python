class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return "ERROR"
        return sum([a * len(b) for a, b in zip(coefs, words)])


    #lst = []
    #for a, b in zip(coefs, words):
    #    lst.append(a * len(b))
    #return sum(lst)

    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return "ERROR"
        lst = []
        for i, a in enumerate(coefs):
            lst.append(len(words[i]) * a)
        return sum(lst)
            
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42, ]
print(Evaluator.enumerate_evaluate(coefs, words))
