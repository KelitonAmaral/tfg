import cv2
import time
import numpy as np


class Lift:
    '''
    The VideoProcessing class contains methods to manipulate and process videos

    Args:
        file_path (str): Path to video file

    Attributes:
        file_path (str): This is where we store the string with the path to the video
    '''
    def __init__(self, file_path):
        self.file_path = file_path

    def find_trajectory(self):
        '''
        Method to select the plates in a video and track its trajectory using CSRT

        Args:
            self (class): reference to the current instance of the class

        Raises:

        Returns:
            trajectory (list):

        '''

        try:
            cap = cv2.VideoCapture(self.file_path)
            print("Video file has been found!")
        except:
            print("Video file not found")

        # Create CSRT tracker, bounding box and trajectory list
        tracker = cv2.TrackerCSRT_create()
        ok, frame = cap.read()
        bbox = cv2.selectROI(frame)
        ok = tracker.init(frame, bbox) 
        # Initialize a list
        trajectory = []

        while True:
            ok, frame = cap.read()
            if not ok:
                break
            ok, bbox = tracker.update(frame)
            
            if ok:
                (x, y, w, h) = [int(f) for f in bbox]
                # print("(x, y):({}, {}) - (w, h): ({}, {})".format(x, y, w, h))
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
                # Append the coordinates of the middle of the bounding box
                trajectory.append([(x+w)/2, (y+h)/2])
            else:
                cv2.putText(frame, "Error", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0XFF == 27: # Tecla 'ESC'
                break
        
        # Libera o objeto de captura do vídeo após operação
        cap.release()

        # Fecha todas as janelas
        cv2.destroyAllWindows()
        

        return trajectory