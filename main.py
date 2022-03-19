import cv2

from project.video_processing.lift import Lift
from project.video_processing.analysis import Analysis




# my_video = Lift(r'project\upload\medias\hang-power-clean.mp4')
my_video = Lift(r'project\upload\medias\video1.mp4')

# print(my_video.trajectory())

my_trajectory = my_video.trajectory()



graph = Analysis()

# trajectory = [[1,2], [1, 4]]

graph.plot_graph(my_trajectory)



# try:
#     # img = cv2.imread('home.jpg')
#     for x,y in list:
#         # print(f"({x},{y})")
#         # histr = cv2.calcHist([img],[x],None,[256],[0,256])
# except:
#     print("Erro")




# import numpy as np.
# import cv2 as cv.
# from matplotlib import pyplot as plt.
# img = cv.imread('home.jpg')
# color = ('b','g','r')
# for i,col in enumerate(color):
# histr = cv.calcHist([img],[i],None,[256],[0,256])


# my_video.kcf_analyze_trajectory()

# my_video.show_trajectory()


# cap = cv2.VideoCapture(r'project\upload\medias\hang-power-clean.mp4')
# tracker = cv2.TrackerKCF_create()
# ok, frame = cap.read()
# print(ok)
# bbox = cv2.selectROI(frame)
# ok = tracker.init(frame, bbox)