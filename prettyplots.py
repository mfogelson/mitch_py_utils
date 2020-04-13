#!/usr/bin/env python 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot2d(x, y, ax=None, color='r', marker='_', title='', xlabel='x', ylabel='y', name='data', xmin=None, xmax=None, ymin=None, ymax=None):
    '''
    Description: A pretty plot function for 2d plots in python\n
    Returns: ax -> current axis
    '''
    if not ax:
        fig = plt.figure()
        ax = fig.add_subplot(111)

    ax.plot(x, y, c=color, marker=marker, label=name)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid()
    if xmin: 
        ax.set_xlim(xmin=xmin)
    if xmax: 
        ax.set_xlim(xmax=xmax)
    if ymin: 
        ax.set_ylim(ymin=ymin)
    if ymax: 
        ax.set_ylim(ymax=ymax)

    return ax

def plot3d(x, y, z, ax=None,color='r', marker='_', title='', xlabel='x', ylabel='y', zlabel='z', name='data', xmin=None, xmax=None, ymin=None, ymax=None, zmin=None, zmax=None):
    '''
    Description: A pretty plot function for 3d plots in python\n
    Returns: ax -> current axis
    '''
    if not ax:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, z, c=color, marker=marker, label=name)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.grid()
    if xmin: 
        ax.set_xlim(left=xmin)
    if xmax: 
        ax.set_xlim(right=xmax)
    if ymin: 
        ax.set_ylim(bottom=ymin)
    if ymax: 
        ax.set_ylim(top=ymax)
    if zmin: 
        ax.set_zlim(zmin=zmin)
    if zmax: 
        ax.set_zlim(zmax=zmax)

    return ax

if __name__ == "__main__":
    x = range(10)
    y = range(10)
    z = range(10)
    plot3d(x,y,z, xmin=2, ymax=5, title='Test data')
    plt.show()
