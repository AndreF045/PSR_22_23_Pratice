#!/usr/bin/env python3

from colorama import Fore, Style, Back

class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        self.r = y.r
        self.i = y.i
            
        # addapt code to use classes

    def multiply(self, y):
        pass

    def __str__(self):
        return f"complex{self.r} + {self.i}"
        # addapt code to use classes

    


def main():







if __name__ == "__main__":
    main()
