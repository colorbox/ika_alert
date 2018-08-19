# -*- coding: utf-8 -*
import glob
import cv2
import numpy as np

# generateimage array
def creeate_image_array(img_paths):
    images = []
    for img_path in img_paths:
        image = cv2.imread(img_path)
        reshaped_image = image.reshape(image.shape[0] * image.shape[1] * 3)
        images.append(reshaped_image)
    return np.array(images, np.float32)

def main():
    # positive and negative image paths
    pos_img_paths = glob.glob('./data/grouped_icons/0/*')
    neg_img_paths = glob.glob('./data/grouped_icons/1/*') + glob.glob('./data/grouped_icons/2/*') + glob.glob('./data/grouped_icons/3/*')

    # load images
    positive_images = creeate_image_array(pos_img_paths)
    negative_images = creeate_image_array(neg_img_paths)
    images = np.r_[positive_images, negative_images]

    # generate labels
    positive_labels = np.ones(len(pos_img_paths), np.int32)
    negative_labels = np.zeros(len(neg_img_paths), np.int32)
    labels = np.array([np.r_[positive_labels, negative_labels]])

    # RTree
    rtree = cv2.ml.RTrees_create()
    rtree.setMaxDepth(50)
    rtree.train(images, cv2.ml.ROW_SAMPLE, labels)
    rtree.save('dead_train.xml')

if __name__ == '__main__':
    main()