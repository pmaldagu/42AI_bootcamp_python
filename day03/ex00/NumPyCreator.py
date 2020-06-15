import numpy as np

class NumPyCreator:
    def from_list(self, lst):
        return np.asarray(lst)

    def from_tuple(self, tpl):
        array = np.asarray(tpl)
        dtype = array.dtype
        print(dtype)
        return np.asarray(tpl, dtype)

    def from_iterable(self, itr):
        return np.fromiter(itr)

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.rand(*shape)

    def identity(self, n):
        return np.identity(n)

#if __name__ == "__main__":
#    nump = NumPyCreator()
#    array = ([1, 2, 3], [6, 3, 4])
#    arrayt= ("a", "b", "c")
#    array = nump.from_list(array)
#    arrayt = nump.from_tuple(arrayt)
#    print(array)
#    print(arrayt)
