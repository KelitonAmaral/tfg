import cv2
import numpy as np
from project.video_processing.lift import Lift
from project.video_processing.analysis import Analysis






# my_video = Lift(r'project\upload\medias\hang-power-clean.mp4')
my_video = Lift(r'project\upload\medias\snatch.mp4')

my_trajectory = my_video.find_trajectory()

# print(my_trajectory)

# print("Trajetória original: ")
# print(len(my_trajectory))
# x = 0
# i = 0
# tamanho = len(my_trajectory)
# while i < tamanho:
#     if i % 3 == 0:
#         x += 1
#         # print(i, " ", my_trajectory[i])
#         del my_trajectory[i]
#         tamanho = len(my_trajectory)
#     i += 1 

# for i in range(20):
    # del my_trajectory[0]

# print("Contador: ", x)
# print(len(my_trajectory))


graph = Analysis()

# trajectory = graph.reverse_y_elements(my_trajectory)

# print("Trajetória com y invertido: ")
print(my_trajectory)
graph.plot_graph(my_trajectory)