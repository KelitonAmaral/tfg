# tfg
Final undergraduation project for the Computer Science course at Universidade Franciscana.

Python-Django Online System with video processing (object tracking) by OpenCV.

How to install and run the code:
1) Install Python 3.8.10 on your computer. Up until June 06, 2022, OpenCV was working only with Python 3.8.10 and below, so this application was not tested for later Python editions;

2) Use a pip command to install the necessary frameworks. Python 3.8 already has pip installed so you can simply open a new terminal and type (without quotation marks) "pip install -r requirements.txt". The file "requirements.txt" on the root directory of the project contains a list of frameworks used.

3) Open "main.py" in your favorite code editor or IDE. Line 7 has the data for an athlete in parenthesis - body weight in kilograms, body height in centimeters and age, while line 14 has the location and name of the MP4 video file the application will analyze. You can change the athlete's stats in line 7 and use another MP4 video from "upload\medias" directory, or simple run the code as is. The application will analyze the lift in the "1080_snatch_82.mp4" video, using 98 kg, 180 cm and 36 years as data for the athlete.

4) When you run the code, you will be prompted on the terminal to enter how much weight (kg) the athlete is lifting in the video. To be acurate with "1080_snatch_82.mp4" video, you can type 82. If you use other videos, make sure to type the weight being lifted. Although the application has no way of knowing if it is true or not, that weight will be used to calculate the relative strength of the athlete using their body weight, informed in line 7, and it will show the result on the terminal.