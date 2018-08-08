import os
import shutil
import numpy as np
from PIL import Image
from skimage import data
from sklearn.cluster import KMeans

print('clustering start')

cluster_count = 4

origin_dir = './data/icons/'
dist_dir = './data/grouped_icons/'

origin_dirs = [(origin_dir + path) for path in os.listdir(origin_dir) if not path.startswith('.')]

# read all icons in origin_dir
origin_images = []
for dir in origin_dirs:
    for path in os.listdir(dir):
        origin_images.append(dir + '/' + path)

feature = np.array([data.imread(path) for path in origin_images])
feature = feature.reshape(len(feature), -1).astype(np.float64)

print('data reshape completed')

model = KMeans(n_clusters=cluster_count).fit(feature)

print('clustering completed')

labels = model.labels_

for label, path in zip(labels, origin_images):
    image_name = path.split('/')[-1]
    dirpath = dist_dir + str(label)
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)

    shutil.copyfile(path, dist_dir + str(label) + "/" + image_name)

print('all completed')
