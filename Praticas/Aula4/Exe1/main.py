#!/usr/bin/env python

from ast import parse
from email import parser
import cv2
import argparse


def main():


    parser=argparse.ArgumentParser(description="path to image")
    parser.add_argument("-img", "--img_path", help = "mode: time", default= "/home/andre/Desktop/PSR/PSR_22_23_Pratice/Praticas/Aula4/images/atlascar2.png")
    args = parser.parse_args()

    image_1 = cv2.imread(args.img_path, cv2.IMREAD_COLOR)
    image_2 = cv2.imread("/home/andre/Desktop/PSR/PSR_22_23_Pratice/Praticas/Aula4/images/atlascar.png", cv2.IMREAD_COLOR)

    cv2.imshow("atlas", image_1)
    cv2.imshow("atlas", image_2)
    cv2.waitKey(0)


  
if __name__ == '__main__':
    main()      
