# -*- coding: utf-8 -*
import glob
import cv2
import numpy as np

# generate image array
def creeate_image_array(img_paths):
    images = []
    for img_path in img_paths:
        image = cv2.imread(img_path)
        reshaped_image = image.reshape(image.shape[0] * image.shape[1] * 3)
        images.append(reshaped_image)
    return np.array(images, np.float32)

def main():
    # set test target images
    test_img_paths = glob.glob('./data/grouped_icons/1/*') + glob.glob('./data/grouped_icons/2/*') + glob.glob('./data/grouped_icons/3/*')
    # test_img_paths = glob.glob('./data/grouped_icons/0/*')

    # loading
    rtree = cv2.ml.RTrees_load("dead_train.xml")
    
    # test
    images = creeate_image_array(test_img_paths)
    predicted = rtree.predict(images)
    result = predicted[1]
    for (i, img_path) in enumerate(test_img_paths):
        if result[i][0] == 1.0:
            print("yes", img_path)
        else:
            print("no", img_path)

if __name__ == '__main__':
    main()
