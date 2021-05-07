import torch
import torchvision
import cv2
import time
import numpy as np
import os
import ssl
import albumentations as A

# Defining the transforms for the image frames and read the class names from the labels.txt file
transform = A.Compose([
    # resize the image to 128×171 dimension, which is in regard to the training dimensions
    A.Resize(128, 171, always_apply=True),
    # apply center cropping to the frames to crop them to 112×112 dimensions
    A.CenterCrop(112, 112, always_apply=True),
    # normalize the dataset according to the expected Kinetics-400 normalization values
    A.Normalize(mean = [0.43216, 0.394666, 0.37645],
                std = [0.22803, 0.22145, 0.216989],
                always_apply=True)])

# read the class names from labels.txt
with open('labels.txt', 'r') as f:
	class_names = f.readlines()
	f.close()

# Turning certificate verification off
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

# Taking video path and clip length input from user
video_input = input("Enter path to input video: ")

# When getting clip_len
print("The model will predict the class action name by looking at 'clip_len' consecutive frames from video clip")
print("This affects both the quality of predictions and the speed of predictions")
clip_len = int(input("Enter number of frames to consider for each prediction: "))

# get labels
class_names = class_names
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# load the model, also if this is your first time using it, then it will be downloaded first
model = torchvision.models.video.r3d_18(pretrained=True, progress=True)
# load the model onto the computation device
model = model.eval().to(device)

cap = cv2.VideoCapture(video_input)
if (cap.isOpened() == False):
    print('Error while trying to read video')
# get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# define codec and create VideoWriter object
try:
    output_name = f"output/output_{video_input.split('/')[1]}"
except:
    print("Check video path!")
    exit(0)
out = cv2.VideoWriter(output_name,
                      cv2.VideoWriter_fourcc(*'mp4v'), 30,
                      (frame_width, frame_height))

frame_count = 0 # to count total frames
total_fps = 0 # to get the final frames per second
clips = [] # a clips list to append and store the individual frames

# read until end of video
while(cap.isOpened()):
    # capture each frame of the video
    ret, frame = cap.read()
    if ret == True:
        # get the start time
        start_time = time.time()
        image = frame.copy()

        # convert the frame to RGB colour from the default BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # transform the image using the transforms
        frame = transform(image=frame)['image']
        # appending the individual frames to the clips list
        clips.append(frame)

        if len(clips) == clip_len:
            with torch.no_grad(): # we do not want to backprop any gradients
                input_frames = np.array(clips)

                # add an extra dimension
                input_frames = np.expand_dims(input_frames, axis=0)

                # transpose to get [1, 3, num_clips, height, width]
                input_frames = np.transpose(input_frames, (0, 4, 1, 2, 3))

                # convert the frames to tensor
                input_frames = torch.tensor(input_frames, dtype=torch.float32)
                input_frames = input_frames.to(device)

                # forward pass to get the predictions
                outputs = model(input_frames)

                # get the prediction index
                _, preds = torch.max(outputs.data, 1)

                # map predictions to the respective class names
                label = class_names[preds].strip()

            # get the end time
            end_time = time.time()

            # get the fps
            fps = 1 / (end_time - start_time)

            # add fps to total fps
            total_fps += fps

            # increment frame count
            frame_count += 1
            wait_time = max(1, int(fps/4))
            cv2.putText(image, label, (15, 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2,
                        lineType=cv2.LINE_AA)
            clips.pop(0)
            cv2.imshow('image', image)
            out.write(image)

            # press `q` to exit
            if cv2.waitKey(wait_time) & 0xFF == ord('q'):
                break
    else:
        break

# release VideoCapture()
cap.release()

# close all frames and video windows
cv2.destroyAllWindows()

# calculate and print the average FPS
try:
    avg_fps = total_fps / frame_count
    print(f"Average FPS: {avg_fps:.2f}")
    print(f"Output video has been saved in -> {output_name}")
except:
    print("Check video path!")
