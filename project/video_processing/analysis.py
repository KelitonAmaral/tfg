import matplotlib.pyplot as plt

class Analysis:

    def plot_graph(self, coordinates):
        x = []
        y = []
        for a,b in coordinates:
            x.append(a)
            y.append(b)

        plt.xlabel("Eixo x")
        plt.ylabel("Eixo y")
        plt.title("Coordenadas cartesianas da trajetória da barra")
        plt.xlim(0, 1000)
        plt.ylim(0, 1000)
        plt.plot(x, y, label="Trajetória")
        
        plt.show()

    def calculate_relative_strength(self, body_weight, bar_weight):
        return round(bar_weight / body_weight, 2)

    # def normalize_list(self, trajectory):
    #     coordinates = [[i / sum(j) for i in j] for j in trajectory]
    #     return coordinates