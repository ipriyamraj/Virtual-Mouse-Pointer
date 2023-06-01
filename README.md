Virtual Mouse System using Hand Gestures and Computer Vision 

Project Overview

The Virtual Mouse System is a project that aims to develop an intuitive and natural way of interacting with a computer by controlling the mouse functions through hand gestures and computer vision technology. This system eliminates the need for a physical mouse and provides a more immersive user experience.
The project utilizes the Python programming language along with libraries such as OpenCV, MediaPipe, PyAutoGUI, and AutoPy for hand tracking, gesture recognition, and mouse control. By leveraging the computer's webcam or built-in camera, the system captures real-time hand movements and tracks the fingertip to perform various mouse operations.

Key Features

Mouse cursor control: Users can move the mouse cursor on the computer screen by simply moving their hand in the air. The system tracks the hand movements and translates them into corresponding cursor movements.
Click functions: The virtual mouse system supports both left-click and right-click actions. By making specific hand gestures, users can perform these actions without the need for a physical mouse. For example, making a fist gesture performs a left-click, while spreading fingers performs a right-click.
Scroll functionality: Hand movements can be used to simulate scrolling up and down on web pages, documents, or any scrollable content. This feature provides a convenient way to navigate through lengthy documents or websites. For instance, moving the index finger up or down performs scrolling actions.
Double-click capability: The system incorporates a gesture recognition algorithm that detects a double-click gesture performed by the user. This allows for quick execution of actions that typically require a double-click, such as opening files or selecting text. For example, tapping the index finger twice in quick succession triggers a double-click action.
Additional mouse functions: The virtual mouse system also supports additional mouse functions, such as drag and drop operations. By performing specific gestures, users can initiate dragging actions and release them at desired locations.

Technology Stack

The Virtual Mouse System is built using the following technologies and libraries:
1.Python programming language: Python serves as the core programming language for the project, providing a versatile and easy-to-use platform for development.
2.OpenCV: OpenCV (Open Source Computer Vision Library) is a powerful library that offers a wide range of image and video processing functions. In this project, OpenCV is used for tasks such as hand detection, hand tracking, and image processing.
3.MediaPipe: MediaPipe is an open-source framework developed by Google that provides a pipeline for building multimodal machine learning applications. It offers pre-built solutions for various computer vision tasks, including hand tracking. In this project, MediaPipe is used for accurate hand detection and tracking.
4.PyAutoGUI: PyAutoGUI is a cross-platform Python library that provides automation capabilities, including controlling the mouse and keyboard. It is used in the virtual mouse system to perform mouse-related actions, such as moving the cursor and simulating mouse clicks.
5.AutoPy: AutoPy is a library that enables cross-platform automation of mouse and keyboard operations. It is used in the virtual mouse system to control mouse functions, such as moving the cursor and performing drag and drop actions.

Getting Started

To get started with the Virtual Mouse System, follow the steps below:
1.Install Dependencies: Before running the system, ensure that you have the required dependencies installed. The main dependencies for this project are OpenCV, MediaPipe, PyAutoGUI, and AutoPy. You can install them using the following commands:
pip install opencv-python
pip install mediapipe
pip install pyautogui
pip install autopy
2.Run the System: Navigate to the project directory and run the main Python script, main.py, using the following command:
python main.py
3.Interact with the Virtual Mouse: Once the system is running, use your webcam or built-in camera to perform hand gestures and control the virtual mouse. Move your hand to move the cursor, perform gestures for left-click, right-click, scroll, double-click, and drag and drop actions.

Gesture Controls
1.Mouse Cursor Movement:
Gesture: If the index finger is up (tip Id = 1) or both the index finger (tip Id = 1) and middle finger (tip Id = 2) are up.
Action: Move your hand in the air to control the mouse cursor on the computer screen.
2.Left Button Click
Gesture: If both the index finger (tip Id = 1) and the thumb finger (tip Id = 0) are up, and the distance between the two fingers is less than 40px.
Action: Perform a pinch gesture with your thumb and index finger to simulate a left-click.
3.Right Button Click
Gesture: If both the index finger (tip Id = 1) and the middle finger (tip Id = 2) are up, and the distance between the two fingers is less than 40px.
Action: Perform a pinch gesture with your index finger and middle finger to simulate a right-click.
4.Scroll Up
Gesture: If both the index finger (tip Id = 1) and the middle finger (tip Id = 2) are up, and the distance between the two fingers is greater than 40px. Move the two fingers upwards.
Action: Simulate a scroll up function by moving your fingers upwards.
5.Scroll Down
Gesture: If both the index finger (tip Id = 1) and the middle finger (tip Id = 2) are up, and the distance between the two fingers is greater than 40px. Move the two fingers downwards.
Action: Simulate a scroll down function by moving your fingers downwards.
6.Double Click
Gesture: If the index finger (tip Id = 1), little finger (tip Id = 4), and thumb finger (tip Id = 0) are up.
Action: Perform a pinch gesture with your thumb, index finger, and little finger to simulate a double left-click. This action occurs after a certain interval of time (0.25 seconds in this project).
7.No Action
Gesture: If all fingers are up (tip Id = 0, 1, 2, 3, and 4).
Action: No mouse events are performed on the screen.

Project Structure
The project directory consists of the following files:
1.main.py: The main entry point of the system. It initializes the necessary components and runs the virtual mouse application.
2.hand_tracking.py: This module contains functions and classes related to hand detection and tracking. It utilizes MediaPipe for accurate hand tracking.
3.mouse_control.py: This module implements the mouse control functionality based on hand gestures. It maps the detected gestures to corresponding mouse actions using PyAutoGUI and AutoPy.
4.utils.py: A collection of utility functions and helper methods used throughout the project.
