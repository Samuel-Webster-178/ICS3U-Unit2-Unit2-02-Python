#!/usr/bin/env python3

# Created by Samuel Webster
# Created on February 2022
# Calculates perimeter and area of a rectangle
#     with dimensions inputted from user


def main():
    # input
    length = int(input("Enter length of the rectangle in mm: "))
    width = int(input("Enter width of the rectangle in mm: "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("Area is {0} mm².".format(area))
    print("Perimeter is {} mm.".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
