# -*- coding: utf-8 -*

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('data/pinch/000217.jpg',0)

template = cv.imread('enemy_pinch2.png',0)
template = cv.imread('friend_pinch1.png',0)

w, h = template.shape[::-1]

method = cv.TM_CCOEFF_NORMED
# Apply template Matching
res = cv.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
if max_val > 0.95:
    print("pinch!!!!")
else:
    print("not pinch ＼(ツ)／")

print(max_val)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if cv.TM_CCOEFF_NORMED in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img,top_left, bottom_right, 255, 2)
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle('cv.TM_CCOEFF_NORMED')
plt.show()