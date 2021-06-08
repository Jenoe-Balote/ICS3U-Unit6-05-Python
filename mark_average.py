#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on: June 2021
# this program averages out marks inputted by the user

import math


def calculate_average(marks):
    # this function calculates the average

    list_sum = 0

    for mark in marks:
        list_sum = list_sum + mark
    average = list_sum / (len(marks))

    # source used for rounding numbers:
    # https://realpython.com/python-rounding/#rounding-up
    return math.ceil(average)


def main():
    # this function collects the marks

    mark_list = []

    # input and process
    print("Let's calculate an average mark!")
    print("Enter marks one by one (0 is the lowest, 100 is the highest)")
    print("Enter -1 once you are done.")
    print("")
    mark_string = input("Enter a mark (%): ")
    while True:
        try:
            mark_int = int(mark_string)
            # end list
            if mark_int == -1:
                break
            # catch invalid input
            elif mark_int < 0 or mark_int > 100:
                mark_string = input("Invalid. Enter a mark (%): ")
            else:
                mark_string = input("Enter a mark (%): ")
                mark_list.append(mark_int)
        # catch invalid input
        except Exception:
            mark_string = input("Invalid. Enter a mark (%): ")

    # call function(s)
    average = calculate_average(mark_list)

    # output
    print("\nThe average is: {}%".format(average))
    print("\nThanks for participating!")


if __name__ == "__main__":
    main()
