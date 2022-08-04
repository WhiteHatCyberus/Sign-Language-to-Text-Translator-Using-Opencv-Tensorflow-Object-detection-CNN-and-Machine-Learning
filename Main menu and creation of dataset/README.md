Disclaimer: Several modules don't work anymore because of the latest depreciation changes of tensorflow and object detection modules for python in 2021.

THIS FOLDER IS TO BE USED TO CREATE CUSTOM DATASETS OF ALPHABETS, WORDS ETC.

# Introduction
This is a simple CNN project which helps its users to convert ASL directly into text. We have used different types of gestures which can be converted into text on the basis of the standard American Sign Language. The project is trained on Tensorflow Object Detection API.
The major technologies used are IMAGE PROCESSING, COMPUTER VISION, OBJECT DETECTION and CNN (Convolutional Neural Network).


1. While creating this project,we learned what a CNN is and how it works. Best resources were 
<a href="https://www.tensorflow.org/get_started/">Tensorflow's official website</a> and <a href="https://machinelearningmastery.com">machinelearningmastery.com</a>.

2. Created a CNN which look a lot similar to <a href="https://www.tensorflow.org/tutorials/layers">this MNIST classifying model</a> using both Tensorflow Object Detection API.This project is easily editable and one can add more gestures.

3. Then used the model which was trained using Tensorflow.

## Requirements

0. Python 3.10
1. <a href="https://tensorflow.org">Tensorflow 1.5</a>
2. <a href="https://keras.io">Keras</a>
3. OpenCV
4. h5py
5. pyttsx3
6. A good CPU (preferably with a GPU).
7. Use contrast background for better results

## Installing the requirements
1. Start your terminal of cmd depending on your os.
2. If you have a NVidia GPU then make sure you have the prerequisites for Tensorflow GPU installation.Then use this commmand

    pip install -r requirements_gpu.txt

3. In case you do not have a GPU then use this command

    pip install -r requirements_cpu.txt


## Creating your own gesture:

  1. First set your hand histogram. You do not need to do it again if you have already done it. But you do need to do it if the lighting conditions change. To do so type the command given below and follow the instructions below.
    
    python set_hand_hist.py

  * A windows "Set hand histogram" will appear.
  * "Set hand histogram" will have 50 squares (5x10).
  * Put your hand in those squares. Make sure your hand covers all the squares.
  * Press 'c'. 1 other window will appear "Thresh".
  * On pressing 'c' only white patches corresponding to the parts of the image which has your skin color should appear on the "Thresh" window. 
  * Make sure all the squares are covered by your hand.
  * In case you are not successful then move your hand a little bit and press 'c' again. Repeat this until you get a good histogram.
  * After you get a good histogram press 's' to save the histogram. All the windows close.
  * All gestures are stored in 'gestures/' folder

