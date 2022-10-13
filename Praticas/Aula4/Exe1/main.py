#!/usr/bin/env python

import cv2

def main():

    img = cv2.imread("/home/andre/Pictures/green_man.jpeg")

    cv2.imshow("shrek", img)
    k = cv2.waitKey(0)

    if k == ord("s"):
        cv2.imwrite("shrek.png", img)

  
if __name__ == '__main__':
    main()      
