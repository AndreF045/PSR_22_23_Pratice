#!/usr/bin/env python

import cv2

def main():

    img = cv2.imread("/home/andre/Pictures/green_man.jpeg")

    if img is None:
        sys.exit("Could not read the image.")

    cv2.imshow("este é o shek", img)
    k = cv.waitKey(0)

    if k == ord("s"):
        cv2.imwrite("shrek.png", img)

  
if __name__ == '__main__':
    main()      
