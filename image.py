import cv2
import numpy as np
import json

img = cv2.imread('screen_map.png')
max_h, max_w, dim = img.shape

for y in range(max_h):
	for x in range(max_w):
		if (img[y,x] == [9,238,33]).all():
			print(y,x)