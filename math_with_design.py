#!/usr/bin/env python3

# Created by Samuel Webster
# Created on February 2022
# Calculates perimeter and area of a rectangle
#     with dimensions inputted from user


def main():

    length = int(input("Enter length of the rectangle in mm: "))
    width = int(input("Enter width of the rectangle in mm: "))
    print("Area is {0} mm².".format(length * width))
    print("Perimeter is {} mm.".format(2 * (length + width)))
    print("\nDone.")


if __name__ == "__main__":
    main()
