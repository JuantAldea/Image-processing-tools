
# This code performs collision image registration calculating the 
# homography between the set of points introduced by clicking on 
# the two images.
# Point correspondence is given by the order of point introduction.
#
# This code was programmed to align some aerial images taken on 
# on different flights
#
# For more information visit:
# https://en.wikipedia.org/wiki/Homography
# https://en.wikipedia.org/wiki/Homography_(computer_vision)
#
# Copyright (C) 2016, Juan Antonio Aldea Armenteros
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf8 -*-

import cv2
import numpy as np

points1 = np.empty((0,2), dtype=float)
points2 = np.empty((0,2), dtype=float)

def mouse_callback(event, x, y, flags, param):
    global points1
    global points2
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        (im, image_index) = param
        if image_index == 1:
            points1 = np.append(points1, [[x, y]], axis=0)
            cv2.circle(im, (x, y), 2, (0, 0, 255), -1)
        else:
            points2 = np.append(points2, [[x, y]], axis=0)
            cv2.circle(im2, (x, y), 2, (0, 0, 255), -1)
    
    print(points1)
    print(points2)

def homo(pts_src, pts_dst, im):
    h, status = cv2.findHomography(pts_src, pts_dst)
    print(h)
    print(status)
    return cv2.warpPerspective(im, h, (im.shape[1], im.shape[0]))

im1 = np.zeros((400, 400, 3), np.uint8)
im2 = np.zeros((400, 400, 3), np.uint8)
im3 = np.zeros((400, 400, 3), np.uint8)

cv2.circle(im1, (200, 200), 100, (255, 0, 0), -1)

im1 = cv2.imread("im.png")
im2 = cv2.imread("im2.png")

cv2.namedWindow("Display1", cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow("Display2", cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow("Display3", cv2.CV_WINDOW_AUTOSIZE)
     
cv2.setMouseCallback("Display1", mouse_callback, (im1, 1))
cv2.setMouseCallback("Display2", mouse_callback, (im2, 2))

while(True):
    cv2.imshow("Display1", im1)
    cv2.imshow("Display2", im2)
    cv2.imshow("Display3", im3)

    if cv2.waitKey(15)%0x100 == ord('a'):
        im3 = homo(points1, points2, im)
    
    #ord(scape) = 27
    if cv2.waitKey(15)%0x100==27:
        break

cv2.destroyWindow("Display1")
cv2.destroyWindow("Display2")
cv2.destroyWindow("Display3")
