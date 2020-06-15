import numpy as np
import pandas as ps
import matplotlib.pyplot as plt
import seaborn as sb
import scipy as sp
from FileLoader import FileLoader

class MyPlotLib:
    def histogram(self, data, features):
        fig, axes = plt.subplots(nrow=1, ncols=len(features))
        for ft in features :
            ft = axes.flatten()
            lst = list(data[ft])
            arr = np.array([x for x in lst if ~np.isnan(x)])
            ft.hist(arr, bins=8)
            ft.set_tittle(ft)
            ft.grid()
        plt.show()

    def density(self, data, features):

    def pair_plot(self, data, features):

    def box_plot(self, data, features):


if __name__ == "__main__":
    fl = FileLoader()
    data = fl.load("../ruc.csv")
    mpl = MyPlotLib()
    features = ['Height', 'Weight']
    mpl.histogram(data, features)

x = np.random.normal(size = 1000)
n_bins = 10

fig, axes = plt.subplots(nrows=1, ncols=2)
ax0, ax1= axes.flatten()

ax0.hist(x, n_bins, density=True, histtype='bar', color='b')
ax0.legend(prop={'size': 10})
ax0.set_title('Height')

ax1.hist(x, n_bins, density=True, histtype='bar', color='b')
ax1.set_title('Weight')

ax0.grid()

plt.show()

