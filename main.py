#code to automate the acquisition of "just the two of us" images from youtube and crop them

import numpy as np
import os
import cv2
# import youtube_dl
from glob import glob
import pafy

from api_key import key # requires a api_key.py file containing the variable 'key' with a google api key as the value

frame_num = 1300 #nth frame to catch 180 = 3s @60fps
pafy.set_api_key(key)

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_stream, save_dir, name): #get frame from video
    create_dir(save_dir)

    try:
        cap = cv2.VideoCapture(video_stream.url)
        cap.set(1, frame_num) #(1, x) x = whichth frame to capture
        ret, frame = cap.read()

        cv2.imwrite(f"{save_dir}\\{name}.png", frame)
    except cv2.error as e:
        print(e)
        cap.release()
        save_frame(vid_stream, save_dir, name)

    cap.release()
    print("Completed Capturing A Frame Of" + str(name))


if __name__ == "__main__": #you know the drill
    # url = "https://www.youtube.com/watch?v=X-pZFNsncu8"
    playlist = pafy.get_playlist2("https://youtube.com/playlist?list=PL-vSysBoeI98daMpbj5V5vtRf-qxI0qAJ")

    vid_count = 1

    for vid in playlist:

        print("Starting on " + str(vid_count))
        vid_stream = pafy.new(vid.videoid)
        video = vid_stream.getbestvideo(preftype="mp4")

        print
        save_frame(video, "saves", vid_count)

        vid_count += 1

    # print("Starting...")
    # vid_stream = pafy.new(url) 
    # video = vid_stream.getbestvideo(preftype="mp4")

    # print("Running...")
    # save_frame(video, "saves")