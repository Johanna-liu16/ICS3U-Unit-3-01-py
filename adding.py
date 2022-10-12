#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program adds two numbers

def main():
    # this function calculates the cost of making a pizza

    # input
    print("This program adds two numbers.")
    int_one = int(input("Enter a number: "))
    int_two = int(input("Enter another number: "))

    # process
    answer = int_one + int_two

    # output
    print("{0:,.0f} + {1:,.0f} = {2:,.0f}".format(int_one, int_two, answer))

    print("\nDone.")


if __name__ == "__main__":
    main()
