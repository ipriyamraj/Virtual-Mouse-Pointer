# Virtual-Mouse-Pointer
This is a system for controlling the mouse pointer through hand gestures, using a camera and advanced hand tracking algorithms.

The code is a Python implementation of a hand tracking algorithm that allows you to control your mouse using hand gestures. The program tracks your fingers and allows you to move your cursor and click the mouse based on certain gestures. It uses the OpenCV library for image processing and the autopy and pynput libraries for controlling the mouse.

To use the program, simply run the code and place your hand in front of your camera. The program will track the movement of your fingers and use them to move and click the mouse. The program also has some additional features, such as scrolling the mouse up and down, which can be done by holding up two fingers, and middle-clicking by holding up both index and middle fingers and bringing them together.

The code uses a "HandTrackingModule" that is imported into the main script. This module contains a class called "handDetector" which provides all the necessary functions to detect and track the hand in real-time. This module is based on the MediaPipe framework and uses a pre-trained neural network to detect hand landmarks.

The code can be run on any system that has a webcam and the required libraries installed. It has been tested on Windows, Linux, and macOS.
