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

        ATTENTION:
        OpenCV treats images as a matrix with a width (number of columns) and 
        height (number of rows). In computer science we locate an element in a matrix
        using an index system that works like this:

        matrix[i][j]

        Where "i" is the row in which the element is located, then "j" represents
        the column. For example, an element in the position [0][3] is located in 
        the first row and fourth column, assuming you are using a programing language
        that starts indexing at zero 

        This coordinate system is different from a traditional cartesian plane.
        To locate a point in a cartesian plane we have x first (column), then y (row):

        point(x, y)

        In other words:
        Coordinates in OpenCV               (y, x)
        Coordinates in Cartesian Plane      (x, y)

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
        
        # Now we need to know the height and width of the VideoCaputre object we created.
        # We can use the function get() passing the id of the property as argument. 
        # See doc: https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html 
        video_width = int(cap.get(3))
        video_height = int(cap.get(4))
        # # # define codec and create VideoWriter object
        # out = cv2.VideoWriter('out_videos/marketing_out.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width, frame_height))
        print(video_height)
        print(video_width)
        # Create CSRT tracker, bounding box and trajectory list
        tracker = cv2.TrackerCSRT_create()
        ok, frame = cap.read()
        bbox = cv2.selectROI(frame)
        ok = tracker.init(frame, bbox) 
        # Initialize a list
        trajectory = []

        # Using cap.get() show information about the video captured
        # in the VideoCapture object, according to the property used
        # as argument. 
        # See doc: 
        # https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Show (height, width, channels) of the first frame of the video.
        # Height and width are given by number of pixels
        # Color images will show 3 channels (red, green and blue)
        # print(frame.shape)

        # The shape function returns a tuple, therefore we can access
        # each value individualy by index. Remember: height comes first
        # then width 
        # video_height = frame.shape[0]
        # video_width = frame.shape[1]
        # video_channels = frame.shape[2]

        # print(video_height)
        # print(video_width)
        # print(video_channels)

        while True:
            ok, frame = cap.read()
            # print(frame)
            if not ok:
                break

            # add gaussian blurring to frame
            frame_blurred = cv2.GaussianBlur(frame, (5, 5), 0)
            
            # Convert to gray scale
            frame = cv2.cvtColor(frame_blurred, cv2.COLOR_BGR2GRAY)
            
            # save video frame
            # out.write(frame)
            
            ok, bbox = tracker.update(frame)
            
            if ok:
                # # Convert to gray scale
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # # add gaussian blurring to frame
                # frame = cv2.GaussianBlur(frame, (5, 5), 0)
                # # save video frame
                # out.write(frame)
                (x, y, bbox_w, bbox_h) = [int(f) for f in bbox]
                # print("(x, y):({}, {}) - (w, h): ({}, {})".format(x, y, w, h))
                cv2.rectangle(frame, (x, y), (x + bbox_w, y + bbox_h), (0, 255, 0), 2, 1)
                new_y = video_height - y

                trajectory.append([x, new_y])
                # Append the coordinates of the middle of the bounding box
                # trajectory.append([(x+w)/2, (y+h)/2])


                # # Remember: col in a matrix representing an image is the "x" in a cartesian plane,
                # # "y" is the row. In the next line, we are getting the origin of the bounding box in the
                # # upper left corner, its width and height 
                # (row, col, w, h) = [int(f) for f in bbox]
                # cv2.rectangle(frame, (row, col), (row + h, col + w), (0, 255, 0), 2, 1)
                # # Append the coordinates of the middle of the bounding box. This is just geometry to 
                # # find the center of the square we named "bounding box" that tracks the object.
                # # Calculate the length of an horizontal edge and divide by 2. Then do the same thing 
                # # with a vertical edge 
                # trajectory.append([(col+w)/2, (row+h)/2])
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