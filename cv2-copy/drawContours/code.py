import cv2
import numpy as np

im = cv2.imread("im.png")
w, h, c = im.shape

# b = np.ones(shape=(h, w, 1), dtype = np.uint8)*255
# g = np.ones(shape=(h, w, 1), dtype = np.uint8)*0
# r = np.ones(shape=(h, w, 1), dtype = np.uint8)*0
# background = np.concatenate((b, g, r), axis=2)

im_copy = im.copy()
im_gray = im[:, :, 0]
ret, im_binary = cv2.threshold(im_gray, thresh=120, maxval=255, type=cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(im_binary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im_masked = im_copy - cv2.fillPoly(im, pts=contours, color=(0,0,0))
im_masked_binary = cv2.fillPoly(im_masked, pts=contours, color=(255,255,255))
cv2.drawContours(im_copy, contours, contourIdx=-1, color=(0,0,255))
# im_masked = im_copy - cv2.fillPoly(im, pts=contours, color=(0,0,0)) + cv2.fillPoly(background, pts=contours, color=(0,0,0))
cv2.imwrite("binary.png", im_masked_binary)
cv2.imwrite("im_contour.png", im_copy)
