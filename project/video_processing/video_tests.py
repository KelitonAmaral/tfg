import os
import cv2

class VideoProcessing:
    @classmethod
    def open_file(self, file_name):    
        
        # Mode to be set 
        mode = 0o666
        
        # flags
        # flags = os.O_RDWR | os.O_CREAT
        flags = os.O_RDWR

        try:
            fd = os.open(file_name, flags, mode)
            os.close(fd)
            print("\nFile descriptor closed successfully.")

        except:
            print("File not found.")


# path = '../upload/medias/hang-power-clean.mp4'

# VideoProcessing.open_file(path)