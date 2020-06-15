import numpy as np

class ColorFilter:
    def invert(array):
        array = 1.0 - array
        return array

    def to_blue(array):
        array[:,:,0] = np.zeros((np.shape(array)[0], np.shape(array)[1]))
        array[:,:,1] = np.zeros((np.shape(array)[0], np.shape(array)[1]))
        return array

    def to_green(array):
        array[:,:,0] = 0
        array[:,:,2] = 0
        return array

    def to_red(array):
        array[:,:,1] = 0
        array[:,:,2] = 0

    def celluloid(array):
        array *= 10
        array //= 1
        array /= 10
        return array

    def celluloid(self, array, threshold=10):
        steps = np.linspace(0, 1, threshold)
        for i in range(len(array)) :
            for j in range(len(array[0])) :
                for k in range(len(array[0][0])) :
                    tmp = 0
                    for step in steps:
                        if array[i][j][k] > step:
                            tmp = step
                    array[i][j][k] = tmp
        return array

        
