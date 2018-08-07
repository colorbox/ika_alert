import os
import shutil
import numpy as np
from PIL import Image
from skimage import data
from sklearn.cluster import KMeans

cluster_count = 4

origin_dir = './data/merged_icons/'
dist_dir = './data/grouped_icons/'
origin_images =  [path for path in os.listdir(origin_dir) if not path.startswith('.')]

feature = np.array([data.imread(origin_dir + path) for path in origin_images])
feature = feature.reshape(len(feature), -1).astype(np.float64)

print('data reshape completed')

model = KMeans(n_clusters=cluster_count).fit(feature)

print('clustering completed')

labels = model.labels_

print(labels)

for label, path in zip(labels, origin_images):
    dirpath = dist_dir + str(label)
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)
    shutil.copyfile(origin_dir + path, dist_dir + str(label) + "/" + path)

print('all completed')
