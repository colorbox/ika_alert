# coding: UTF-8

import cv2
import numpy as np
import time

def is_friend_pinch(template):
    img = cv2.imread('friend_pinch1.png',0)

    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.95:
        return True
    else:
        return False

def is_enemy_pinch(template):
    img = cv2.imread('enemy_pinch2.png',0)

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

def result_from_fixed(name):
    images = []
    image = cv2.imread("data/watching/" + name + ".png")
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
    filepath = "./data/watching/" + name + ".png"
    image = cv2.resize(image,(80,90))
    cv2.imwrite(filepath, image)
    return filepath

def main():
    ESC_KEY = 27     # Escキー
    INTERVAL= 1     # 待ち時間

    ORG_WINDOW_NAME = "movie"

    DEVICE_ID = 1

    # capture
    # cap = cv2.VideoCapture(DEVICE_ID)
    cap = cv2.VideoCapture('./data/movies/8_t.mov')

    end_flag, c_frame = cap.read()

    # ウィンドウの準備
    cv2.namedWindow(ORG_WINDOW_NAME, cv2.WINDOW_NORMAL)

    # 変換処理ループ
    while end_flag == True:
        # フレーム表示
        cv2.imshow(ORG_WINDOW_NAME, c_frame)

        # print(c_frame.shape)
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
        r1 = result_from_fixed("1")

        rectangle2 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(friends_start_column + icon_start_column_gap + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle2, "2")
        r2 = result_from_fixed("2")

        rectangle3 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(friends_start_column + (icon_start_column_gap) * 2 + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle3, "3")
        r3 = result_from_fixed("3")

        rectangle4 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(friends_start_column + (icon_start_column_gap) * 3 + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle4, "4")
        r4 = result_from_fixed("4")

        rectangle5 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(enemy_start_column + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle5, "5")
        r5 = result_from_fixed("5")

        rectangle6 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(enemy_start_column + (icon_start_column_gap) * (1) + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle6, "6")
        r6 = result_from_fixed("6")

        rectangle7 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(enemy_start_column + (icon_start_column_gap) * (2) + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle7, "7")
        r7 = result_from_fixed("7")

        rectangle8 = cv2.getRectSubPix(c_frame, (int(icon_width), int(icon_height)),( int(enemy_start_column + (icon_start_column_gap) * (3) + (icon_width/2)), int(icon_rows_from + (icon_height/2))))
        save_fixed_name_image(rectangle8, "8")
        r8 = result_from_fixed("8")

        # print(r1,r2,r3,r4,r5,r6,r7,r8)
        # print("------------")

        # print(type(c_frame))

        gray = cv2.cvtColor(c_frame, cv2.COLOR_BGR2GRAY)
        print(is_enemy_pinch(gray),is_friend_pinch(gray))

        # if (r1+r2+r3+r4 < r5+r6+r7+r8):
        #     print("人数有利")
        # elif (r1+r2+r3+r4 > r5+r6+r7+r8):
        #     print("人数不利")

        # wait for esc key
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        # read next frame
        end_flag, c_frame = cap.read()

    cv2.destroyAllWindows()
    cap.release()

if __name__ == '__main__':
    main()
