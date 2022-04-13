import cv2
import numpy as np
from project.video_processing.lift import Lift
from project.video_processing.analysis import Analysis






# my_video = Lift(r'project\upload\medias\hang-power-clean.mp4')
my_video = Lift(r'project\upload\medias\snatch.mp4')

my_trajectory = my_video.find_trajectory()

# print("Trajetória original: ")
# print(my_trajectory)

graph = Analysis()

# trajectory = graph.reverse_y_elements(my_trajectory)

# print("Trajetória com y invertido: ")
# print(trajectory)

graph.plot_graph(my_trajectory)