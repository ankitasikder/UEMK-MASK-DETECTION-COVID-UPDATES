# PROJECT-3-UEMK-MASK-DETECTION-COVID-UPDATES

***This new Handwriting Recognizer using Python is created by Ankita Sikder and also other group members special credit goes to Biswarup Bhattacharjee(@biswa2210), student of BTECH, in University of Engineering and Management, Kolkata.***

**Email Id: ankita.sikder14@gmail.com.** 

**Contact No: 8583939774.** 


<p align="left">
<a href="https://facebook.com/ankita.sikder.104" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="biswa2210" height="30" width="40" /></a>
<a href="https://instagram.com/ankita.sikder14" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="" height="30" width="40" /></a>
<a href="https://github.com/biswa2210/ankitasikder" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="" height="30" width="40" /></a>
</p>

# PROJECT-1-UEMK-HANDWRITING RECOGNIZER :computer: :open_file_folder: :pencil2: 

[![Generic badge](https://img.shields.io/badge/deep-learning-red)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/artificial-neural%20retwork-yellow)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/convolutional%20-neural%20network-orange)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/MNIST-dataset-green)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Graphical%20-UI-brightgreen)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Tesseract-OCR-blue)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/python-3.6-green)](https://shields.io/) 


## About :point_down: 

<div align="justified">
   
**This is basically a group project for Project-1 in UEMK. I have contributed some parts. All names of the group members are in developers section.** Handwriting recognition (HWR), also known as Handwritten Text Recognition (HTR), is the ability of a computer to receive and interpret intelligible handwritten input from sources such as paper documents, photographs, touch-screens and other devices. The image of the written text may be sensed "off line" from a piece of paper by optical scanning (optical character recognition) or intelligent word recognition. Alternatively, the movements of the pen tip may be sensed "on line", for example by a pen-based computer screen surface, a generally easier task as there are more clues available. A handwriting recognition system handles formatting, performs correct segmentation into characters, and finds the most possible words. I have made a handwritten recognizer for recognising both handwritten text and OCR. By running a python program in computer user can use it. I have made a GUI to make it user friendly. It can recognize characters and numbers written with hand or optical character. After detection we get 99% accurate results. It can be implemented in many areas in present digital world. Python-tesseract is used to recognize and read the text. In handwriting recognition (HWR) the device interprets the user's handwritten characters or words into a format that the computer understands (e.g., Unicode text). The input can be from paper documents, images, touch-screens and other devices. There are many levels of HWR, starting from the recognition of simplified individual characters to the recognition of whole words and sentences of cursive handwriting. Character recognition often involves scanning a form or document. This means the individual characters contained in the scanned image will need to be extracted. After the extraction of individual characters occurs, a recognition engine is used to identify the corresponding character. OCR systems consist of following major stages : • Classification • Post-processing • Feature Extraction. This Handwriting recognition is used for numerous applications such as : reading postal addresses, bank check amounts, and forms. Furthermore, OCR plays an important role for digital libraries, allowing the entry of image textual information into computers by digitization, image restoration, and recognition methods. 
</div>

## Working Principle :point_down:

<div align="justified">
   
Coming to the the main working part of our project. Here main three parts are present. First one is GUI part which means the Graphical User Interface part of our project. Second one is Handwritten Digit Recognition part. It contains also a GUI part that is Handwritten Recognition GUI and second one is functionality part. In this functionality part two functionalities are present, first one is pictorial detection functionality that recognizes Handwritten digits from an image and second one is the live detection functionality that recognizes handwritten digits from a video. Let us come to the ocr part of our project. Ocr stands for Optical Character Recognition , here we use Tesseract algorithm to detect handwritten characters as well as type written character also. In this part after recognizing the characters it will pronunciated by python text to speech library that is the pyttsx3 library in python. Let me deep dive into the GUI part. GUI is basically type of user interface through which users interact with electronic devices via visual indicater representation . It allows the user of a computer to communicate with the computer by moving a pointer around on a screen and clicking a button. In our project it is created by Tkinter package In python.This has a developer section which is also made by Tkinter.In our project handwritten digit recognition part is made by the concept of deep learning. Basically deep learning is a subset of machine learning. In this part we will create a deep learning model using the MNIST dataset which is present in the keras model in python. The set of images in the MNIST dataset is a combination of two of NIST's databases. The MNIST databases are special database 1 and special database 3.It consists of digits written by High School students and employees of United States Census Bureau. The MNIST dataset contains total 70000 images in those 60000 images are training images and 10000 images are testing images. All images are normalized to fit into 28 into 28 pixels. Let us a come to the model creation part. Here we use CNN analysis to create our deep learning model. CNN is basically Convolutional Neural Network. It's used for matrix manipulation or manipulation. The first step of CNN is input image from our MNIST dataset after that it will pass through the Convolutional layers. In our project 64 Convolutional 2 d filters are used . In CNN this part us called feature detecting part or filtering part. After that this filtered image will pass through the neural network.Then generate a fully connected layer and get the output layer. For creating our deep learning model we use the activation function relu that is rectified linear unit in Convolutional 2 d function for solving vanishing gradient problem where the kernel size is 3,3. In the output layer of our model we use softmax activation function in dense function for predicting the multiple outputs. At last for compiling our model we use SGD that is Stochastic Gradient Decent optimzer which is an iterative method for optimizing an objective function with suitable smoothness properties. In browsing image part in our project we use the opencv function in python to recognize input image which is inputted by filedialogue function in Tkinter. This is all about working of Machine learning part of my project.
</div>

## Why I have made this project :point_down:

<div align="justified">
   
The goal of this project is to create a model that will be able to recognize and determine the handwritten digits from its image by using the concepts of Convolution Neural Network and Optical Character recognition with tesseract-OCR. Though the goal is to create a model which can recognize the digits, it can be extended to letters and an individual’s handwriting. The major goal of the proposed system is understanding Convolutional Neural Network, and applying it to the handwritten recognition system. The another goal of this project is that make a simple user friendly graphical user interface to handle recognizing handwritten digits and OCR, create a developers section in graphical user interface where the all group members details are written. I have made this so that user can use this handwriting recognition approach using this very fast and easily. It can be used in many fields for study, investigation, database management cases etc.
</div>

## Applications and Future Scopes:point_down:

•Check reading.<br>
•Census data collection and processing.<br>
•Image document reading.<br>
•Digitizing old books in editable form.<br>
•Extended research:<br>
   •text to speech conversion (e-book reading).<br>
   •Visually impaired should be able to access computers in their native language.<br>
• Develop an online system for searching hundreds of books over the Web.<br>
• Recognition and retrieval of complex documents (such as camera-based, handwritten, etc.).<br>

## Folder Structure :point_down:

```bash
PROJECT-1-UEMK
     ├── .idea
     ├── NeedSoftware
     ├── Test Images
     ├── Test_Videos
     ├── _pycache_
     ├── ocr
     ├── Display Mnist.py
     ├── MNIST_CNN.model
     ├── MNIST_CNN.py
     ├── developers.py
     ├── developerswalp.jpg
     ├── gui_interface.py
     ├── handwrittenDigitRecognitionWallpaper.jpg
     ├── mini_developerswalp.jpg
     ├── mini_handwrittenDigitRecognitionWallpaper.jpg
     ├── mini_img.jpg
     ├── mini_img1.jpg
     ├── mini_img2.jpg
     ├── mini_img3.jpg
     ├── mini_img4.jpg
     ├── mini_img5.jpg
     ├── ocr.jpg
     ├── ocr_gui.py
     ├── ocrecog.py
     ├── ocrwallpaper.jpg
     ├── pok.ico
     ├── pok.jpeg
     ├── pok.wav
     ├── pok2.wav
     ├── pok2.ico
     ├── pok3.ico
     ├── recognizefromvideo.py
     ├── recognizer.py
     ├── recognizer_gui.py
     └── rootwallpaper.jpg 
```                       

**:point_right: [click here to read Project1 Research Paper](https://github.com/ankitasikder/PROJECT-1-UEMK-HR/blob/main/3rdSemProject1ResearchPaper.pdf)<br>
:point_right: [click here to see Project1 PowerPoint Presentation](https://drive.google.com/file/d/1xHzAZ_VeGLOKnhNyvG6ip11RjY5P5mgV/view)<br>
:point_right: [click here to view or download Project1 Demo Video](https://github.com/ankitasikder/PROJECT-1-UEMK-HR/blob/main/SAMPLE%20OUTPUT/3SEM%20PROJECT.mp4)**

## Making :point_down:

<div align="justified">
   
**I have made this using python3.** I have used CNN, ANN concepts, deep learning, MNIST datasets, lamda function, numpy, pandas, matplotlib, sklearn, keras, tensorflow, tkinter, SGD(Stockastic Gradient Decent), opencv , pillow, pyttsx3, kernel etc for this project. Here I have used training and testing data sets for model detection. Now let me come to the OCR part of this project. I have used CNN(Convolutional Neural Network) for matrix manupulation.

## Screenshots :point_down: 

<div align="center">
<a href="pics/hr1.PNG"><img src="pics/hr1.PNG" width="400" height= "300"></a> <a href="pics/hr2.PNG"><img src="pics/hr2.PNG" width="400" height= "300"></a>

<a href="pics/hr3.PNG"><img src="pics/hr3.PNG" width="400" height= "300"></a> <a href="pics/hr4.PNG"><img src="pics/hr4.PNG" width="400" height= "300"></a>

<a href="pics/hr5.PNG"><img src="pics/hr5.PNG" width="400" height= "300"></a> <a href="pics/hr6.PNG"><img src="pics/hr6.PNG" width="400" height= "300"></a>

<a href="pics/hr7.PNG"><img src="pics/hr7.PNG" width="400" height= "300"></a> <a href="pics/hr8.PNG"><img src="pics/hr8.PNG" width="400" height= "300"></a>
</div>

## Block Diagram of Project :point_down:

<div align="center">
<a href="pics/bl.PNG"><img src="pics/bl.PNG" width="800" height= "350"></a>
</div>


