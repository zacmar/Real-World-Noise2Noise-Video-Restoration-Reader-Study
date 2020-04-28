import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import os


def my_plot(stacked_results):
    mean = np.mean(stacked_results, axis=0)
    print(mean / 8)
    buttons = ['Overall\nBest',
               'Least\nFlickering',
               'Significant\nSmoothing']
    methods = ['Original', 'GT Learning', 'N2N Learning']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.array([[i] * 3 for i in range(3)]).ravel() * 2
    y = np.array([i for i in range(3)] * 3) * 2
    z = np.zeros(3 * 3)
    dx = np.ones(3 * 3)
    dy = np.ones(3 * 3)
    dz = mean.ravel()
    ax.bar3d(x, y, z, dx, dy, dz)
    plt.xticks([0, 2, 4], methods)
    plt.yticks([0, 2, 4], buttons)
    plt.show()


def _main():
    path = './secure/'
    listing = os.listdir(path)
    num_ratings = len(listing)
    stacked_results = np.empty((num_ratings, 3, 3))
    for i_rating, name in enumerate(listing):
        full_path = os.path.join(path, name)
        stacked_results[i_rating] = np.load(full_path)
    my_plot(stacked_results)


if __name__ == '__main__':
    _main()
