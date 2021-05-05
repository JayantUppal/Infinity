# Task 3: Human Activity Recognition

Identify and recognize human activity from a videosource and classify it based on the activity thus performed.

## Solution

I started from searching for some pre-trained models for action recognition and I found that PyTorch provided a few. I will be using the ResNet 3D PyTorch
model. The ResNet 3D model that PyTorch provides is an 18 layers model. This model has been trained on the Kinetics-400 dataset.
The Kinetics-400 dataset contains 400 classes of human actions and each class contains at least 400 clips. Each of these clips are around 10 seconds and
they have been taken from YouTube videos. I will be using these pre-trained weights to recognize actions in our own videos.

### How to use

- Create a virtual environment
```
$ pip install virtualenv
$ virtualenv har-env
$ source har-env/bin/activate
```
- Clone this repo
```
git clone https://github.com/JayantUppal/Infinity.git
cd Infinity/
cd AlphaAI/
cd Human-Activity-Recognition/
```
- Install necessary imports (It will take some time)
```
pip install -r requirements.txt
```
- Now, you're good to go
```
python HAR.py
```
- I have added four input and output examples in input and output folder respectively.
- If you want to test on any video, put your video in **input** folder and execute using:-
```
python HAR.py

Enter path to input video: input/<test video name with .mp4 goes here>

Output video has been saved in -> output_<test video name>
```

## References
- [PyTorch video classification docs](https://github.com/pytorch/vision/blob/master/docs/source/models.rst#video-classification)
- [DeepMind Kinetics papers and datasets](https://deepmind.com/research/open-source/kinetics)
- [Human Action Recognition in Videos using PyTorch](https://debuggercafe.com/human-action-recognition-in-videos-using-pytorch/)
- [Human Activity Recognition with OpenCV and Deep Learning](https://www.pyimagesearch.com/2019/11/25/human-activity-recognition-with-opencv-and-deep-learning/)
