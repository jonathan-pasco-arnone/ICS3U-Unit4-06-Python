#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program displays every possible rgb color code


def main():
    # This function displays every possible rgb color code

    counter1 = -1
    counter2 = -1
    counter3 = -1
    print("")
    print("This Program Prints every possible rgb color.")
    print("")
    input("Press enter to proceed")

    while counter1 < 255:
        counter1 = counter1 + 1
        while counter2 < 255:
            counter2 = counter2 + 1
            while counter3 < 255:
                counter3 = counter3 + 1
                print("RGB({0},{1},{2})".format(counter1, counter2, counter3))
            counter3 = 0
        counter2 = 0


if __name__ == "__main__":
    main()
