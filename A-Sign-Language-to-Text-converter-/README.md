Due to python's module depreciation, some modules of object detection may not work, so we had to host the application in Jupyter-notebook for the main phase of sign language to text converter.
Introduction:
To save time and ease of convenience of creating a custom dataset, we had downloaded a dataset from kaggle.com (best preference: create your own custom datasets)

Dataset  for Sign Language to Text conversion  is obtained from the ASL alphabet, Image Data set for  alphabets in the American sign language 
https://www.kaggle.com/datasets/grassknoted/asl-alphabet

Approach:
1. We obtain the dataset from the ASL alphabet, Image Data set for alphabets in the American sign language.
2.Dataset preprocessing/cleaning(maximizing its information content) +Data augmentation(zooming ,rotating)+ Data Visualization using Seaborn/Matplotlib.
3. Using the CNN approach for training the model on the above-augmented data.
4. Using OpenCV we are getting the bounding box of hand signals in the webcam. Then we feed these boxes to the trained model for classification.

Note: make sure 'Documents' folder (folder contains asl_train and asl_test) should be in the same folder as the .ipynb file.
