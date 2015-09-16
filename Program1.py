#
__author__ = 'Marisa Gross'

# CIS 125
# Program1
#
# Table of Celsius and Fahrenheit equivalents from 0C to 100C


def main():
    for C in range(0,101,10):
        F = (9/5 * C) + 32
        print(C,F)
        
main()