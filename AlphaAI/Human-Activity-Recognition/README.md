# Task 3: Human Activity Recognition

Identify and recognize human activity from a videosource and classify it based on the activity thus performed.

## Solution

I started by searching for some pre-trained models for action recognition and I found that PyTorch provided a few. I will be using the ResNet 3D PyTorch model. The ResNet 3D model that PyTorch provides is an 18 layers model. This model has been trained on the Kinetics-400 dataset. The Kinetics-400 dataset contains 400 classes of human actions and each class contains at least 400 clips. Each of these clips is around 10 seconds and they have been taken from YouTube videos. I will be using these pre-trained weights to recognize actions in our videos.

### How to use

- Create a virtual environment
```
$ pip install virtualenv
$ virtualenv har-env
$ source har-env/bin/activate
```
![Create a virtual environment](https://user-images.githubusercontent.com/47852407/117101440-e0e78880-ad93-11eb-9602-342e830bca1f.png)

- Clone this repo
```
$ git clone https://github.com/JayantUppal/Infinity.git
$ cd Infinity/
$ cd AlphaAI/
$ cd Human-Activity-Recognition/
```
![Clone this repo](https://user-images.githubusercontent.com/47852407/117101515-fe1c5700-ad93-11eb-89fb-8835706a0147.png)

- Install necessary imports (It will take some time)
```
$ pip install -r requirements.txt
```
![Install necessary imports](https://user-images.githubusercontent.com/47852407/117101554-168c7180-ad94-11eb-8bee-50e13ca08883.png)

- Now, you're good to go
```
$ python HAR.py
```
![Execution](https://user-images.githubusercontent.com/47852407/117101605-3459d680-ad94-11eb-948a-74a529a65774.png)

- I have added four input and output examples in input and output folder respectively.
- If you want to test on any video, put your video in **input** folder and execute using:-
```
$ python HAR.py

Enter path to input video: input/<test video name with .mp4 goes here>

Output video has been saved in -> output_<test video name>
```

## Test cases
![pushup](https://user-images.githubusercontent.com/47852407/117101837-b3e7a580-ad94-11eb-9153-387a28ae68b7.png)
![stretchingarm](https://user-images.githubusercontent.com/47852407/117101913-daa5dc00-ad94-11eb-861a-5da73f8bcf6a.png)
![yoga](https://user-images.githubusercontent.com/47852407/117102014-07f28a00-ad95-11eb-894b-f18b4b174893.png)
![iceclimbing](https://user-images.githubusercontent.com/47852407/117102113-3d977300-ad95-11eb-926e-f90d04bd1525.png)
![snowboarding](https://user-images.githubusercontent.com/47852407/117102150-556ef700-ad95-11eb-8c51-926133d50377.png)


## References
- [PyTorch video classification docs](https://github.com/pytorch/vision/blob/master/docs/source/models.rst#video-classification)
- [DeepMind Kinetics papers and datasets](https://deepmind.com/research/open-source/kinetics)
- [Human Action Recognition in Videos using PyTorch](https://debuggercafe.com/human-action-recognition-in-videos-using-pytorch/)
- [Human Activity Recognition with OpenCV and Deep Learning](https://www.pyimagesearch.com/2019/11/25/human-activity-recognition-with-opencv-and-deep-learning/)
