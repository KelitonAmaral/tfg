import matplotlib.pyplot as plt
from sklearn import preprocessing
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import time
import numpy as np


class Analysis:

    def normalize_list(self, trajectory):
        coordinates = [[i / sum(j) for i in j] for j in trajectory]
        return coordinates
    
    # def reverse_y_elements(self, original_list):
    #     x = []
    #     y = []  
    #     for a,b in original_list:
    #         # print(a, b)
    #         x.append(a)
    #         y.append(b)
    #     y.reverse()
    #     # print(x)
    #     # print(y)
    #     new_list = list(map(list, zip(x, y)))
    #     return new_list


    # def normalize_list_numpy(self, trajectory):
    #     print("Coordenadas ANTES do reverse")
    #     print(trajectory)
    #     trajectory.reverse()
    #     print("Coordenadas DEPOIS do reverse")
    #     print(trajectory)
    #     coordinates = [[i / sum(j) for i in j] for j in trajectory]
    #     coordinates = np.array(coordinates)
    #     return coordinates


    def plot_graph_numpy(self, coordinates):
        # data to be plotted
        # x = np.arange(1, 11)
        # y = x * x
        x = coordinates[:,0]
        y = coordinates[:,1]

        # plotting
        plt.title("Line graph")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.plot(x, y, color ="red")
        plt.show()



    def plot_graph(self, coordinates):
        x = []
        y = []
        my_tuple = tuple(coordinates)
        print(my_tuple)
        for a,b in coordinates:
            # print(a, b)
            x.append(a)
            y.append(b)
            
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()

    def plot_graph3(self, coordinates):
        # coordinates.reverse()
        x = []
        y = []
        for a,b in coordinates:
            print(a, b)
            x.append(a)
            y.append(b)
            
        fig, ax = plt.subplots()
        ax.plot(x, y)

        path = Path(coordinates, codes=None)

        patch = patches.PathPatch(path, facecolor='white', lw=2)
        ax.add_patch(patch)
        plt.show()


    def plot_graph1(self, coordinates):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(-1,1)
        ax.set_ylim(0,1)
        # plt.ion()
        # # plt.show(block=True)
        # plt.show()

        # verts = [(0, 0), (27, 10)]

        # codes = [Path.MOVETO, Path.LINETO] 

        # codes = [None]  

        path = Path(coordinates, codes=None)

        patch = patches.PathPatch(path, facecolor='white', lw=2)

        # #fig = plt.figure()
        # #ax = fig.add_subplot(111)
        # patch = patches.PathPatch(path, facecolor='white', lw=2)
        ax.add_patch(patch)
        # # ax.set_xlim(-100,100)
        # # ax.set_ylim(-100,100)
        
        # plt.draw()
        plt.show()
        # time.sleep(1)
        plt.pause(0.05)
    
    def plot_graph2(self, coordinates):
        w = 4
        h = 3
        d = 70
        plt.figure(figsize=(w, h), dpi=d)
        fig, ax = plt.subplots()
        ax.axis([-3, 3, -7, -1])
        # string_path_data = [
        #     (mpath.Path.MOVETO, (0, -3)),
        #     (mpath.Path.CURVE4, (1, -4)),
        #     (mpath.Path.CURVE4, (-1, -5)),
        #     (mpath.Path.CURVE4, (0, -6))]


        # string_path_data = [
        #     (mpath.Path.MOVETO, (0, -3)),
        #     (mpath.Path.LINETO, (1, -4)),
        #     (mpath.Path.LINETO, (-1, -5)),
        #     (mpath.Path.LINETO, (0, -6))]

        # codes, verts = zip(*string_path_data)
        # string_path = mpath.Path(verts, codes)
        string_path = mpath.Path(coordinates, codes=None)
        patch = mpatches.PathPatch(string_path, facecolor="white", lw=2)

        ax.add_patch(patch)
        # plt.savefig("out.png")
        plt.show()
