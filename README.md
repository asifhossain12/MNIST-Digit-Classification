# 🧠 MNIST Digit Classification with Deep Learning

## 🚀 Project Overview

This repository contains a deep learning model for classifying handwritten digits using the famous MNIST dataset. The model is built using TensorFlow and Keras and achieves accurate results in predicting the digits 0-9 from input images. 🖼️🔢

## 🌟 Features

📊 MNIST Dataset: 70,000 grayscale images of handwritten digits (60,000 for training, 10,000 for testing).

🤖 Deep Learning Model: A Convolutional Neural Network (CNN) built using TensorFlow and Keras.

💻 Accuracy: Achieves high accuracy on the test set.

🎨 Interactive Visualization: Displays the input digits and the corresponding predictions.

## 🛠️ Tools & Technologies

Python 🐍

TensorFlow and Keras for building the neural network 🔧

NumPy for numerical operations 🧮

Matplotlib for plotting visualizations 📊

Jupyter Notebook for interactive code and visualization 💻


## 📂 Project Structure

mnist_classification.ipynb: The main Jupyter notebook that contains the model and code for training and testing.
README.md: This file that explains the project.


## 🧠 Model Overview

The Convolutional Neural Network (CNN) model has the following architecture:

Input Layer: 28x28 grayscale image of a digit.

Conv2D Layers: For extracting features.

MaxPooling Layers: For down-sampling.

Flatten Layer: To convert the 2D matrix to a 1D vector.

Dense Layers: Fully connected layers for classification.

Output Layer: 10 units (one for each digit class) with softmax activation.


## 🔍 Results

The model achieves 99% accuracy on the MNIST test dataset after training for a few epochs.


## 📸 Example
Here's an example of the input and model prediction:

![MNIST Sample](images/image3.png)



## 📚 Learn More

MNIST Dataset

TensorFlow Documentation

Keras Documentation

## ✨ Contributing

Feel free to contribute by opening an issue or submitting a pull request!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

Happy coding! 😄👨‍💻👩‍💻

