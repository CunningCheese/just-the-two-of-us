#code to automate the acquisition of "just the two of us" images from youtube and crop them
import numpy as np
import os
import cv2
# import youtube_dl
from glob import glob
import pafy

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating director with name {path}")

def save_frame(video_stream, save_dir): #get frame from video
    create_dir(save_dir)

    cap = cv2.VideoCapture(video_stream.url)
    frame_num = 260 #nth frame to catch

    cap.set(1, frame_num) #(1, x) x = which frame to capture

    ret, frame = cap.read()

    cv2.imwrite(f"{save_dir}\\{frame_num}.png", frame)

    cap.release()


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=X-pZFNsncu8" #youtube url

    vid_stream = pafy.new(url)
    video = vid_stream.getbest(preftype="mp4")
    save_frame(video, "saves")

    # video_paths = glob("videos/*")
    # save_dir = "save"

    # for path in video_paths:
    #     save_frame(path, save_dir)