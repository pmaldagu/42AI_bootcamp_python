import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImageProcessor:
    def load(self, path):
        img = mpimg.imread(path)
        dimension = np.shape(img)
        print(dimension)
        print("Loading image of dimensions {0} x {1}".format(dimension[0], dimension[1]))
        return img

    def display(self, array):
        plt.imshow(array)
        plt.show()

imp = ImageProcessor()
img = imp.load("./42AI.png")
print(img)
imp.display(img)

