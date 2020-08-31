import matplotlib.pyplot as plt
from numpy import array, linspace, zeros_like

def plotter(x, y):
    plt.plot(x, y, '-b')
    plt.grid(True)
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.show()