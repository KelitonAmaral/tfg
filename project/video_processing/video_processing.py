import os
import cv2
import time

class VideoProcessing:
    '''
    The VideoProcessing class contains methods to manipulate and process videos

    Args:
        file_path (str): Path to video file

    Attributes:
        file_path (str): This is where we store the string with the path to the video
    '''
    def __init__(self, file_path):
        self.file_path = file_path
    
    def open_file(self):
        '''
        Method to simply play the video like a regular video player using OpenCV.

        Args:
            self (class): reference to the current instance of the class

        Raises:

        Returns:

        '''   
        
        try:
            cap = cv2.VideoCapture(self.file_path)
            fps = int(cap.get(cv2.CAP_PROP_FPS))
        except:
            print("Video file not found")

        while True:
            ok, frame = cap.read()
            if not ok:
                break
            
            time.sleep(0.5/fps)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0XFF == 27: # Tecla 'ESC'
                break
        
        # Libera o objeto de captura do vídeo após operação
        cap.release()

        # Fecha todas as janelas
        cv2.destroyAllWindows()



    def kcf_analyze_trajectory(self):
        '''
        Method to select an object in a video and track his trajectory.

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

        # Create KCF tracker and bounding box
        tracker = cv2.TrackerKCF_create()
        ok, frame = cap.read()
        bbox = cv2.selectROI(frame)
        ok = tracker.init(frame, bbox) 


        while True:
            ok, frame = cap.read()
            if not ok:
                break
            ok, bbox = tracker.update(frame)
            
            if ok:
                (x, y, w, h) = [int(f) for f in bbox]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
                # print(bbox)
                trajectory = [x, y]
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

    def show_trajectory(self):
        for i in self.trajectory:
            print(i)
    
    
    # def play_video():

    #     # Reproduz o vídeo para o usuário mostrando a trajetória rastreada
    
    
    
    # def analyze_lift():
    #     # Analisa atributos do levantamento

    # def show_lift_data():
    #     # Mostra os atributos do levantamento para o usuário
    
    # def show_athlete_stats():
    #     # Mostra as estatísticas de toda a vida de um atleta para o usuário

        


# path = '../upload/medias/hang-power-clean.mp4'

# VideoProcessing.open_file(path)