#!/usr/bin/env python3

import argparse
from operator import truediv  # import argparse library

from my_functions import isPerfect


def main():

    # maximum_number = 2  # maximum number to test.

    parser = argparse.ArgumentParser(description='Test for PSR.')
    parser.add_argument('--maximum_number', type=int, required=True,
                        help='The maximum number until which we check if numbers are perfect.')
    parser.add_argument("--other_number", type=int, required=False),
    

    args = vars(parser.parse_args())
    print(args)


    # write the code ...
    if args["verbose"]:
        print(args["prefix"] + "Testing for perfect numbers!")

    for number in range(1, maximum_number+1):
        if not args["other number"] is None:
            if args["verbose"]:
                print["printing other_number = " + str(args["other_number"])]
        
        print("analysing number" + str(number))
        if isPerfect[number]:
            if args["verbose"]:
                print(str(number) + "is perfect!")
        else:
            if args["verbose"]:
                print(str(number) + "is perfect")
            



if __name__ == '__main__':
    main()


