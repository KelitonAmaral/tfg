import matplotlib.pyplot as plt


class Analysis:
    
    # def plot_graph(self):
    #     nested = [[35, 36, 37], [34, 35, 36, 37, 38], [22, 23, 23, 24]]
    #     fully_nested = [list(zip(*[(ix+1, y) for ix, y in enumerate(x)]))
    #         for x in nested]
    #     names = ['sublist%d' % (i+1) for i in range(len(fully_nested))]

    #     for l in fully_nested:
    #         plt.plot(*l)
    #     plt.xlim(0, 5)
    #     plt.xlabel("Indices")
    #     plt.ylim(0, 40)
    #     plt.xlabel("Values")
    #     plt.legend(names, fontsize=7, loc='upper left')
    #     plt.show()

    def plot_graph(self, coordinates):
        coordinates.reverse()
        x = []
        y = []
        for a,b in coordinates:
            print(a, b)
            x.append(a)
            y.append(b)
        # plt.plot(x, y)
        # x.reverse()
        # y.reverse()
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()
        
        # nested = [[35, 36, 37], [34, 35, 36, 37, 38], [22, 23, 23, 24]]
        # fully_nested = [list(zip(*[(ix+1, y) for ix, y in enumerate(x)]))
        #     for x in coordinates]
        # names = ['sublist%d' % (i+1) for i in range(len(fully_nested))]

        # for x,y in coordinates:
        #     # plt.plot(*l)
        #     plt.plot(x, y)
        # plt.xlim(0, 5)
        # plt.xlabel("Indices")
        # plt.ylim(0, 40)
        # plt.xlabel("Values")
        # plt.legend("Trajetoria", fontsize=7, loc='upper left')
        # plt.show()

    #     # nested = [[35, 36, 37], [34, 35, 36, 37, 38], [22, 23, 23, 24]]
    #     # fully_nested = [list(zip(*[(ix+1, y) for ix, y in enumerate(x)]))
    #     #     for x in coordinates]
    #     # names = ['sublist%d' % (i+1) for i in range(len(fully_nested))]

    #     for l in coordinates:
    #         plt.plot(*l)
    #     plt.xlim(0, 5)
    #     plt.xlabel("Indices")
    #     plt.ylim(0, 40)
    #     plt.xlabel("Values")
    #     # plt.legend(names, fontsize=7, loc='upper left')
    #     plt.legend("Trajectory", fontsize=7, loc='upper left')
    #     plt.show()
