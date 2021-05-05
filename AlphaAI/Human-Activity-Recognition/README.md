# Task 3: Human Activity Recognition

Identify and recognize human activity from a videosource and classify it based on the activity thus performed.

## Solution

I started from searching for some pre-trained models for action recognition and I found that PyTorch provided a few. I will be using the ResNet 3D PyTorch
model in this tutorial. The ResNet 3D model that PyTorch provides is an 18 layers model. This model has been trained on the Kinetics-400 dataset.
The Kinetics-400 dataset contains 400 classes of human actions and each class contains at least 400 clips. Each of these clips are around 10 seconds and
they have been taken from YouTube videos. I will be using these pre-trained weights to recognize actions in our own videos.

### How to use

- Create a virtual environment
```
$ pip install virtualenv
$ virtualenv har-env
$ source har-env/bin/activate
```
- Clone this repo using the link -> https://github.com/JayantUppal/Infinity.git
```
cd Infinity
cd AlphaAI
cd Human-Activity-Recognition
```
- Install necessary imports using requirements.txt
```
pip install -r requirements.txt
```
- Now, you're good to go
```
python HAR.py
```
