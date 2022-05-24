import cv2
import numpy as np


if __name__=="__main__":
    path_to_img = f"494.png"
    img = cv2.imread(path_to_img)
    img_h, img_w, img_c = img.shape

    img_copy = img.copy()
    img_gray = img[:, :, 0]
    ret, img_binary = cv2.threshold(img_gray, thresh=160, maxval=255, type=1) # type=1(0) indicates that pixels>thresh are set to zero(maxval), pixels<thresh are set to maxval(zero).
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    rectangle_contours = []
    gap = 3
    for cnt in contours:
        if len(cnt)>=20:
            x,y,w,h = cv2.boundingRect(cnt)
            x_left = x-gap if x-gap>=0 else 0
            x_right = x+w+gap if x+w+gap<=img_w-1 else img_w-1
            y_up = y-gap if y-gap>=0 else 0
            y_down = y+h+gap if y+h+gap<=img_h-1 else img_h-1
            if x_left==0 and x_right==img_w-1:
                continue
            else:
                rectangle_contours.append(np.array([[x_left, y_up], [x_left, y_down], [x_right, y_down], [x_right, y_up]]))
    
    # draw bounding boxes on the image
    if len(rectangle_contours)>0:
        cv2.drawContours(img_copy, rectangle_contours, contourIdx=-1, color=(0,255,0)) # -1 plots all contours.
    cv2.imwrite("img_bbox.png", img_copy)
