import matplotlib.pyplot as plt
import matplotlib.image as npimg
import numpy as np

class ScrapBooker:
    def crop(self, array, dimensions, position):
        if type(position) is not tuple or len(position) is not 2 or array.shape[0] < (position[0] + dimensions[0]) or  array.shape[1] < (position[1] + dimensions[1]):
            return "error"
        else:
            return array[position[1]: position[1] + dimensions[1], position[1]:position[0] + dimensions[0]]

    def thin(self, array, n, axis):
        i = 0
        while n*i < np.shape(array)[axis]:
            array = np.delete(array, n*i, axis)
            i += 1
        return array

    def juxtapose(array, n , axis):
        i = 0
        newarray = array
        while i < n - 1:
            newarray = np.concatenate((array, newarray), axis)
            i += 1
        return newarray

    def mosaic(array, dimensions):
        array = self.juxtapose(array, dimensions[0], 0)
        array = self.juxtapose(array, dimensions[1], 1)
        return array

if __name__ == "__main__":
    sc = ScrapBooker()
    img = npimg.imread("./42AI.png")
    crop = sc.crop(img, (50, 200), (0, 0))
    plt.imshow(crop)
    plt.show()
    
