import cv2

class Lift:

    def __init__(self, file_path, bar_weight):
        self.file_path = file_path
        self.bar_weight = bar_weight
        # self.lift_date = lift_date

    def find_trajectory(self):
        try:
            cap = cv2.VideoCapture(self.file_path)
            print("Video file found!")
        except:
            print("Video file not found!")

        # CV_CAP_PROP_FPS Frame rate.
        # CV_CAP_PROP_FOURCC 4-character code of codec.
        # CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
        # CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
        # print(cap.get(5))
        # print(cap.get(6))
        # print(cap.get(7))
        # print(cap.get(8))
            
        # Now we need to know the height of the VideoCaputre object we created.
        # We can use the function get() passing the id of the property as argument. 
        # See doc: https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html 
        video_height = int(cap.get(4))

        # Create CSRT tracker instance
        tracker = cv2.TrackerCSRT_create()
        # Read first frame
        ok, frame = cap.read()
        # Create bounding box with region of interest
        bbox = cv2.selectROI(frame)
        # Initialize the tracker with a 
        # known bounding box that surrounded the target.
        ok = tracker.init(frame, bbox) 
        
        # Initialize a list to save the coordinates
        trajectory = []

        while True:
            ok, frame = cap.read()
            if not ok:
                break
            
            # Add gaussian blurring to frame
            frame_blurred = cv2.GaussianBlur(frame, (5, 5), 0)
            
            # Convert to gray scale
            frame = cv2.cvtColor(frame_blurred, cv2.COLOR_BGR2GRAY)
            
            ok, bbox = tracker.update(frame)
            
            if ok:
                (x, y, bbox_w, bbox_h) = [int(f) for f in bbox]
                cv2.rectangle(frame, (x, y), (x + bbox_w, y + bbox_h), (0, 255, 0), 2, 1)
                new_y = video_height - y

                trajectory.append([(x+bbox_w)/2, new_y+bbox_h/2])

            else:
                cv2.putText(frame, "Error", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow('Video', frame)
            # 'ESC' key to stop
            if cv2.waitKey(1) & 0XFF == 27:
                break
        
        # Release the VideoCapture object windows
        cap.release()
        cv2.destroyAllWindows()

        return trajectory

    # def resize_video(self):
    #     cap = cv2.VideoCapture(self.file_path)
    #     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #     out = cv2.VideoWriter('video_snatch.mov',fourcc, 15, (640,480))

    #     while True:
    #         ret, frame = cap.read()
    #         if ret == True:
    #             b = cv2.resize(frame,(640,480),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    #             out.write(b)
    #         else:
    #             break
    #     # Release the VideoCapture object and VideoWriter object
    #     cap.release()
    #     out.release()
    #     cv2.destroyAllWindows()


    