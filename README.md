<h1>Virtual Mouse System using Hand Gestures and Computer Vision</h1> 

<h2>Project Overview</h2>

The Virtual Mouse System is a project that aims to develop an intuitive and natural way of interacting with a computer by controlling the mouse functions through hand gestures and computer vision technology. This system eliminates the need for a physical mouse and provides a more immersive user experience.
The project utilizes the Python programming language along with libraries such as OpenCV, MediaPipe, PyAutoGUI, and AutoPy for hand tracking, gesture recognition, and mouse control. By leveraging the computer's webcam or built-in camera, the system captures real-time hand movements and tracks the fingertip to perform various mouse operations.

<h2>Key Features</h2>

Mouse cursor control: Users can move the mouse cursor on the computer screen by simply moving their hand in the air. The system tracks the hand movements and translates them into corresponding cursor movements.
Click functions: The virtual mouse system supports both left-click and right-click actions. By making specific hand gestures, users can perform these actions without the need for a physical mouse. For example, making a fist gesture performs a left-click, while spreading fingers performs a right-click.
Scroll functionality: Hand movements can be used to simulate scrolling up and down on web pages, documents, or any scrollable content. This feature provides a convenient way to navigate through lengthy documents or websites. For instance, moving the index finger up or down performs scrolling actions.
Double-click capability: The system incorporates a gesture recognition algorithm that detects a double-click gesture performed by the user. This allows for quick execution of actions that typically require a double-click, such as opening files or selecting text. For example, tapping the index finger twice in quick succession triggers a double-click action.
Additional mouse functions: The virtual mouse system also supports additional mouse functions, such as drag and drop operations. By performing specific gestures, users can initiate dragging actions and release them at desired locations.

<h2>Technology Stack</h2>

The Virtual Mouse System is built using the following technologies and libraries:

<ol>
<li><h3>Python programming language:</h3> Python serves as the core programming language for the project, providing a versatile and easy-to-use platform for development</li>
<li><h3>OpenCV:</h3> OpenCV (Open Source Computer Vision Library) is a powerful library that offers a wide range of image and video processing functions. In this project, OpenCV is used for tasks such as hand detection, hand tracking, and image processing.</li>
<li><h3>MediaPipe:</h3> MediaPipe is an open-source framework developed by Google that provides a pipeline for building multimodal machine learning applications. It offers pre-built solutions for various computer vision tasks, including hand tracking. In this project, MediaPipe is used for accurate hand detection and tracking.</li>
<li><h3>PyAutoGUI:</h3> PyAutoGUI is a cross-platform Python library that provides automation capabilities, including controlling the mouse and keyboard. It is used in the virtual mouse system to perform mouse-related actions, such as moving the cursor and simulating mouse clicks.</li>
<li><h3>AutoPy:</h3> AutoPy is a library that enables cross-platform automation of mouse and keyboard operations. It is used in the virtual mouse system to control mouse functions, such as moving the cursor and performing drag and drop actions.</li>
</ol>
  
<h2>Getting Started</h2>

To get started with the Virtual Mouse System, follow the steps below:
<ol>
<li><h3>Install Dependencies:</h3> Before running the system, ensure that you have the required dependencies installed. The main dependencies for this project are OpenCV, MediaPipe, PyAutoGUI, and AutoPy. You can install them using the following commands:
  <ul>
<li>pip install opencv-python</li>
<li>pip install mediapipe</li>
<li>pip install pyautogui</li>
<li>pip install autopy</li>
  </ul>
</li>
<li><h3>Run the System:</h3> Navigate to the project directory and run the main Python script, main.py, using the following command:
python main.py</li>
<li><h3>Interact with the Virtual Mouse:</h3> Once the system is running, use your webcam or built-in camera to perform hand gestures and control the virtual mouse. Move your hand to move the cursor, perform gestures for left-click, right-click, scroll, double-click, and drag and drop actions.</li>

<h2>Gesture Controls</h2>
<ol>
<li><h3>Mouse Cursor Movement</h3>
<h5>Gesture:</h5> When only the index finger is up, the mouse pointer moves around the screen.
</li>

<li><h3>Left Button Click</h3>
<h5>Gesture:</h5> When only the index and middle fingers are up, the mouse pointer performs the left click and the distance between the two fingers should be less than 40px.
</li>

<li><h3>Right Button Click</h3>
<h5>Gesture:</h5> When only the thumb and index fingers are up, the mouse pointer performs the right click and the distance between the two fingers should be less than 40px.
</li>

<li><h3>Scroll Up</h3>
<h5>Gesture:</h5> When only the little finger is up, the mouse pointer performs the scroll up operation and the scrolling function will keep happening as long as the finger is up.
</li>

<li><h3>Scroll Down</h3>
<h5>Gesture:</h5> When only the middle finger is up, the mouse pointer performs the scroll down operation and the scrolling function will keep happening as long as the finger is up.
</li>

<li><h3>Double Click</h3>
<h5>Gesture:</h5> When the thumb, index and little fingers are up, the mouse pointer performs the double left click and the double click will perform after an interval of 0.25 seconds.
</li>

<li><h3>No Action</h3>
<h5>Gesture:</h5> If all fingers are up then no operations will be performed.</li>

</ol>

<h2>Project Structure</h2>
The project directory consists of the following files:
  <ol>
<li><h3>main.py:</h3> The main entry point of the system. It initializes the necessary components and runs the virtual mouse application.</li>
<li><h3>hand_tracking.py:</h3> This module contains functions and classes related to hand detection and tracking. It utilizes MediaPipe for accurate hand tracking.</li>
<li><h3>mouse_control.py:</h3> This module implements the mouse control functionality based on hand gestures. It maps the detected gestures to corresponding mouse actions using PyAutoGUI and AutoPy.</li>
<li><h3>utils.py:</h3> A collection of utility functions and helper methods used throughout the project.</li>
</ol>
