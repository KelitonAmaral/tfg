import cv2
import time


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
        # self.name = name
        # self.athlete = athlete
        # self.weight = weight        
        # self.date_time = date_time

    def trajectory(self):
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
        except:
            print("Video file not found")

        # Create CSRT tracker, bounding box and trajectory list
        tracker = cv2.TrackerCSRT_create()
        ok, frame = cap.read()
        bbox = cv2.selectROI(frame)
        ok = tracker.init(frame, bbox) 
        trajectory = []

        while True:
            ok, frame = cap.read()
            if not ok:
                break
            ok, bbox = tracker.update(frame)
            
            if ok:
                (x, y, w, h) = [int(f) for f in bbox]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
                # cv2.line(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
                # trajectory = [[x, y]]
                trajectory.append([x, y])
                # print(bbox)
                # trajectory.extend([x, y])
                # print(trajectory)
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

    # def trajectory(self):
    #     '''
    #     Method to select an object in a video and track his trajectory using KCF.

    #     Args:
    #         self (class): reference to the current instance of the class

    #     Raises:

    #     Returns:
    #         trajectory (list):

    #     '''

    #     try:
    #         cap = cv2.VideoCapture(self.file_path)
    #     except:
    #         print("Video file not found")

    #     # Create KCF tracker, bounding box and trajectory list
    #     tracker = cv2.TrackerKCF_create()
    #     ok, frame = cap.read()
    #     bbox = cv2.selectROI(frame)
    #     ok = tracker.init(frame, bbox) 
    #     trajectory = []

    #     while True:
    #         ok, frame = cap.read()
    #         if not ok:
    #             break
    #         ok, bbox = tracker.update(frame)
            
    #         if ok:
    #             (x, y, w, h) = [int(f) for f in bbox]
    #             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    #             # trajectory = [[x, y]]
    #             trajectory.append([x, y])
    #             # print(bbox)
    #             # trajectory.extend([x, y])
    #             # print(trajectory)
    #         else:
    #             cv2.putText(frame, "Error", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    #         cv2.imshow('Video', frame)
    #         if cv2.waitKey(1) & 0XFF == 27: # Tecla 'ESC'
    #             break
        
    #     # Libera o objeto de captura do vídeo após operação
    #     cap.release()

    #     # Fecha todas as janelas
    #     cv2.destroyAllWindows()
    
    #     return trajectory

    # def open_file(self):
    #     '''
    #     Method to play the video like a regular video player using OpenCV.
    #     It will play the video at a faster rate, depending on the process power of the computer.
    #     To play the video at a resonable pace, change the values in the sleep() method.

    #     Args:
    #         self (class): reference to the current instance of the class

    #     Raises:

    #     Returns:

    #     '''   
        
    #     try:
    #         cap = cv2.VideoCapture(self.file_path)
    #         fps = int(cap.get(cv2.CAP_PROP_FPS))
    #     except:
    #         print("Video file not found")

    #     while True:
    #         ok, frame = cap.read()
    #         if not ok:
    #             break
    #         # Change values in the sleep() method to change the pace of the video being played
    #         time.sleep(0.5/fps)
    #         cv2.imshow('Video', frame)
    #         if cv2.waitKey(1) & 0XFF == 27: # Tecla 'ESC'
    #             break

    #     cap.release()

    #     cv2.destroyAllWindows()