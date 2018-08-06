# coding: UTF-8

import cv2
import time


def save_image(image):
    filename = time.strftime("%Y%m%d%H%M%S%f.png", time.gmtime())
    file_path = "./data/raw_icons/" + filename
    cv2.imwrite(filepath, image)


def main():
    cap = cv2.VideoCapture('./data/2_t.mp4')
    end_flag, current_frame = cap.read()
    heihgt, width, channels = current_frame.shape
    while end_flag == True:
        rectangle = cv2.getRectSuvPix(current_frame, (53,60), (356 + 26, 15 + 30))

if __name__ == '__main__':
    main()
    