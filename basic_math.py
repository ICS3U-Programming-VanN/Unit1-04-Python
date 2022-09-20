#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: September 16, 2022
# This program prints basic math operations.


# Imports Math library
import math


# Outputs Several math operations
def main():
    print("Addition: 12121 + 1000 = {}".format(12121 + 1000))
    print("Subtraction: 50 - 25 = {}".format(50 - 25))
    print("Division: 4 / 3 = {:.2f}".format(4 / 3))
    print("Multiplication: 15 * 2 = {}".format(15 * 2))
    print("Exponent: 2^10 = {}".format(2**10))
    print("Square Root: √25 = {}".format(math.sqrt(25)))
    print("Decimal Number: √20 = {:.2f}".format(math.sqrt(20)))


# Points out that this file should be ran
if __name__ == "__main__":
    main()
