# coding: UTF-8

import cv2
import numpy as np
import time
import imutils
from imutils.video import FileVideoStream
from imutils.video import FPS
import argparse

def is_friend_pinch(template):
    return (detect_image(template,'template_images/friend_pinch1.png') or detect_image(template,'template_images/friend_pinch2.png') or detect_image(template,'template_images/friend_pinch3.png'))

def is_enemy_pinch(template):
    return (detect_image(template,'template_images/enemy_pinch1.png') or detect_image(template,'template_images/enemy_pinch2.png') or detect_image(template,'template_images/enemy_pinch3.png'))

def detect_image(template, image_name):
    img = cv2.imread(image_name,0)

    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.95:
        return True
    else:
        return False

def is_dead_with_rtree(image, bin_n=32):
    rtree = cv2.ml.RTrees_load("dead_train.xml")
    reshaped_image = image.reshape(image.shape[0] * image.shape[1] * 3)
    reshaped_image = [].append(reshaped_image)
    reshaped_image = np.array(reshaped_image, np.float32)
    pred = rtree.predict(reshaped_image)
    return pred

def result_from_saved_image(name):
    images = []
    image = cv2.imread("./tmp/" + name + ".png")
    reshaped_image = image.reshape(image.shape[0] * image.shape[1] * 3)
    images.append(reshaped_image)
    hist = np.array(images, np.float32)
    rtree = cv2.ml.RTrees_load("dead_train.xml")
    pred = rtree.predict(hist)
    return pred[1][0][0]

def save_image(image):
    filename = time.strftime("%Y%m%d%H%M%S.png", time.gmtime())
    filepath = "./data/icons_from_opencv/" + filename
    cv2.imwrite(filepath,image)
    return filepath

def save_fixed_name_image(image,name):
    filepath = "./tmp/" + name + ".png"
    image = cv2.resize(image,(80,90))
    cv2.imwrite(filepath, image)
    return filepath

def calcurate_icon_status_friend_pinch(c_frame):
        width = c_frame.shape[1]
        height = c_frame.shape[0]

        friend_icon_width = 47.0/1280.0 * width
        friend_icon_height = 52.0/720.0 * height
        friend_icon_start_column_gap = (47.0+4.0)/1280.0 * width
        friend_icon_rows_from = 20.0/720.0 * height
        friends_start_column = 380.0/1280.0 * width

        # 矩形切り取り
        rectangle1 = cv2.getRectSubPix(c_frame, (int(friend_icon_width), int(friend_icon_height)),( int(friends_start_column + (friend_icon_width/2)), int(friend_icon_rows_from + (friend_icon_height/2))))
        save_fixed_name_image(rectangle1,"1")
        r1 = result_from_saved_image("1")

        rectangle2 = cv2.getRectSubPix(c_frame, (int(friend_icon_width), int(friend_icon_height)),( int(friends_start_column + friend_icon_start_column_gap + (friend_icon_width/2)), int(friend_icon_rows_from + (friend_icon_height/2))))
        save_fixed_name_image(rectangle2, "2")
        r2 = result_from_saved_image("2")

        rectangle3 = cv2.getRectSubPix(c_frame, (int(friend_icon_width), int(friend_icon_height)),( int(friends_start_column + (friend_icon_start_column_gap) * 2 + (friend_icon_width/2)), int(friend_icon_rows_from + (friend_icon_height/2))))
        save_fixed_name_image(rectangle3, "3")
        r3 = result_from_saved_image("3")

        rectangle4 = cv2.getRectSubPix(c_frame, (int(friend_icon_width), int(friend_icon_height)),( int(friends_start_column + (friend_icon_start_column_gap) * 3 + (friend_icon_width/2)), int(friend_icon_rows_from + (friend_icon_height/2))))
        save_fixed_name_image(rectangle4, "4")
        r4 = result_from_saved_image("4")

        enemy_icon_width = 58.0/1280.0 * width
        enemy_icon_height = 65.0/720.0 * height
        enemy_icon_start_column_gap = (58.0+7.0)/1280.0 * width
        enemy_icon_rows_from = 14.0/720.0 * height
        enemy_start_column = 694.0/1280.0 * width

        rectangle5 = cv2.getRectSubPix(c_frame, (int(enemy_icon_width), int(enemy_icon_height)),( int(enemy_start_column + (enemy_icon_width/2)), int(enemy_icon_rows_from + (enemy_icon_height/2))))
        save_fixed_name_image(rectangle5, "5")
        r5 = result_from_saved_image("5")

        rectangle6 = cv2.getRectSubPix(c_frame, (int(enemy_icon_width), int(enemy_icon_height)),( int(enemy_start_column + (enemy_icon_start_column_gap) * (1) + (enemy_icon_width/2)), int(enemy_icon_rows_from + (enemy_icon_height/2))))
        save_fixed_name_image(rectangle6, "6")
        r6 = result_from_saved_image("6")

        rectangle7 = cv2.getRectSubPix(c_frame, (int(enemy_icon_width), int(enemy_icon_height)),( int(enemy_start_column + (enemy_icon_start_column_gap) * (2) + (enemy_icon_width/2)), int(enemy_icon_rows_from + (enemy_icon_height/2))))
        save_fixed_name_image(rectangle7, "7")
        r7 = result_from_saved_image("7")

        rectangle8 = cv2.getRectSubPix(c_frame, (int(enemy_icon_width), int(enemy_icon_height)),( int(enemy_start_column + (enemy_icon_start_column_gap) * (3) + (enemy_icon_width/2)), int(enemy_icon_rows_from + (enemy_icon_height/2))))
        save_fixed_name_image(rectangle8, "8")
        r8 = result_from_saved_image("8")

        return [r1,r2,r3,r4,r5,r6,r7,r8]


def calcurate_icon_status_enemy_pinch(c_frame):
        width = c_frame.shape[1]
        height = c_frame.shape[0]

        friend_icon_width = 58.0/1280.0 * width
        friend_icon_height = 65.0/720.0 * height
        friend_icon_start_column_gap = (58.0+7.0)/1280.0 * width
        friend_icon_rows_from = 14.0/720.0 * height
        friends_start_column = 332.0/1280.0 * width

        # 矩形切り取り
        rectangle1 = cv2.getRectSubPix(c_frame, (int(friend_icon_width), int(friend_icon_height)),( int(friends_start_column + (friend_icon_width/2)), int(friend_icon_rows_from + (friend_icon_height/2))))
        save_fixed_name_image(rectangle1,"1")
        r1 = result_from_saved_image("1")

        rectangle2 = cv2.getRectSubPix(c_frame, (int(friend_icon_width), int(friend_icon_height)),( int(friends_start_column + friend_icon_start_column_gap + (friend_icon_width/2)), int(friend_icon_rows_from + (friend_icon_height/2))))
        save_fixed_name_image(rectangle2, "2")
        r2 = result_from_saved_image("2")

        rectangle3 = cv2.getRectSubPix(c_frame, (int(friend_icon_width), int(friend_icon_height)),( int(friends_start_column + (friend_icon_start_column_gap) * 2 + (friend_icon_width/2)), int(friend_icon_rows_from + (friend_icon_height/2))))
        save_fixed_name_image(rectangle3, "3")
        r3 = result_from_saved_image("3")

        rectangle4 = cv2.getRectSubPix(c_frame, (int(friend_icon_width), int(friend_icon_height)),( int(friends_start_column + (friend_icon_start_column_gap) * 3 + (friend_icon_width/2)), int(friend_icon_rows_from + (friend_icon_height/2))))
        save_fixed_name_image(rectangle4, "4")
        r4 = result_from_saved_image("4")

        enemy_icon_width = 47.0/1280.0 * width
        enemy_icon_height = 52.0/720.0 * height
        enemy_icon_start_column_gap = (47.0+4.0)/1280.0 * width
        enemy_icon_rows_from = 22.0/720.0 * height
        enemy_start_column = 699.0/1280.0 * width

        rectangle5 = cv2.getRectSubPix(c_frame, (int(enemy_icon_width), int(enemy_icon_height)),( int(enemy_start_column + (enemy_icon_width/2)), int(enemy_icon_rows_from + (enemy_icon_height/2))))
        save_fixed_name_image(rectangle5, "5")
        r5 = result_from_saved_image("5")

        rectangle6 = cv2.getRectSubPix(c_frame, (int(enemy_icon_width), int(enemy_icon_height)),( int(enemy_start_column + (enemy_icon_start_column_gap) * (1) + (enemy_icon_width/2)), int(enemy_icon_rows_from + (enemy_icon_height/2))))
        save_fixed_name_image(rectangle6, "6")
        r6 = result_from_saved_image("6")

        rectangle7 = cv2.getRectSubPix(c_frame, (int(enemy_icon_width), int(enemy_icon_height)),( int(enemy_start_column + (enemy_icon_start_column_gap) * (2) + (enemy_icon_width/2)), int(enemy_icon_rows_from + (enemy_icon_height/2))))
        save_fixed_name_image(rectangle7, "7")
        r7 = result_from_saved_image("7")

        rectangle8 = cv2.getRectSubPix(c_frame, (int(enemy_icon_width), int(enemy_icon_height)),( int(enemy_start_column + (enemy_icon_start_column_gap) * (3) + (enemy_icon_width/2)), int(enemy_icon_rows_from + (enemy_icon_height/2))))
        save_fixed_name_image(rectangle8, "8")
        r8 = result_from_saved_image("8")

        return [r1,r2,r3,r4,r5,r6,r7,r8]

def calcurate_icon_status(c_frame):
        width = c_frame.shape[1]
        height = c_frame.shape[0]

        icon_width = 53.0/1280.0 * width
        icon_height = 60.0/720.0 * height
        icon_start_column_gap = (53.0+5.0)/1280.0 * width
        icon_rows_from = 16.0/720.0 * height
        friends_start_column = 356.0/1280.0 * width
        enemy_start_column = 697.0/1280.0 * width

        # 矩形切り取り
        rectangle1 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(friends_start_column + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle1,"1")
        r1 = result_from_saved_image("1")

        rectangle2 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(friends_start_column + icon_start_column_gap + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle2, "2")
        r2 = result_from_saved_image("2")

        rectangle3 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(friends_start_column + (icon_start_column_gap) * 2 + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle3, "3")
        r3 = result_from_saved_image("3")

        rectangle4 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(friends_start_column + (icon_start_column_gap) * 3 + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle4, "4")
        r4 = result_from_saved_image("4")

        rectangle5 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(enemy_start_column + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle5, "5")
        r5 = result_from_saved_image("5")

        rectangle6 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(enemy_start_column + (icon_start_column_gap) * (1) + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle6, "6")
        r6 = result_from_saved_image("6")

        rectangle7 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(enemy_start_column + (icon_start_column_gap) * (2) + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle7, "7")
        r7 = result_from_saved_image("7")

        rectangle8 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(enemy_start_column + (icon_start_column_gap) * (3) + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle8, "8")
        r8 = result_from_saved_image("8")

        return [r1,r2,r3,r4,r5,r6,r7,r8]


def main():
    ORG_WINDOW_NAME = "movie"
    ICON_MOVIE = "icon"

    DEVICE_ID = 1

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
    args = vars(ap.parse_args())

    fvs = FileVideoStream(args["video"]).start()
    fps = FPS().start()

    # ウィンドウの準備
    cv2.namedWindow(ORG_WINDOW_NAME, cv2.WINDOW_NORMAL)
    # cv2.namedWindow(ICON_MOVIE, cv2.WINDOW_NORMAL)

    while fvs.more():
        c_frame = fvs.read()
        gray = cv2.cvtColor(c_frame, cv2.COLOR_BGR2GRAY)
        if is_enemy_pinch(gray):
            hoge = calcurate_icon_status_enemy_pinch(c_frame)
        elif is_friend_pinch(gray):
            hoge = calcurate_icon_status_friend_pinch(c_frame)
        else:
            hoge = calcurate_icon_status(gray)
        print(hoge)
        cv2.putText(c_frame, "Queue Size: {}".format(fvs.Q.qsize()),
		(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow(ORG_WINDOW_NAME, c_frame)
        cv2.waitKey(50)
        fps.update()

    fps.stop()
    cv2.destroyAllWindows()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    
if __name__ == '__main__':
    main()
