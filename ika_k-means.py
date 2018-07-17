import os
import shutil
import numpy as np
from PIL import Image
from skimage import data
from sklearn.cluster import KMeans

cluster_count = 4

feature = np.array([data.imread("./icons/" + path) for path in os.listdir('./icons')])
feature = feature.reshape(len(feature), -1).astype(np.float64)

print('data reshape completed')

model = KMeans(n_clusters=cluster_count).fit(feature)

print('clustering completed')

labels = model.labels_

for label, path in zip(labels, os.listdir('./icons')):
    dist_dir_name = "icon_groups"
    dirpath = dist_dir_name + "/" + str(label)
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)
    shutil.copyfile("./icons/" + path, dist_dir_name + "/" + str(label) + "/" + path)
    print(label, path)

print('all completed')
