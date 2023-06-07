"""
Programmer: Madison McCurry
Assignment: Module 12 - Assign 11
Date Completed: 11/14/21
Course: CITC 2391 - C02
Instructor: Martin Bell
"""


def greatest_common_divisor(x, y):
    if y == 0:  # Using stack overflow I found this as a solution, I'm including my own attempt for feedback
        return x  # It may have been the wording, but I wanted to include this bit to have it function correctly
    else:           # As I got around to this assignment late but found this solution rather quickly
        return greatest_common_divisor(y, x % y)


"""  My original attempt
remainder = x % y
if remainder == 0
    exit()
    return y
else:
    greatest_common_divisor(remainder, y)
"""


def main():
    print("Greatest Common Divisor: ")
    while True:
        first_number = int(input("Enter Number 1: "))  # ask for numbers 1 and 2, then feed those into the function
        second_number = int(input("Enter number 2: "))  # Make this a loop
        if first_number < second_number:  # Make sure first num is less than second num
            print("The first number needs to be less than the second number.")
            first_number = int(input("Enter Number 1: "))
            second_number = int(input("Enter number 2: "))
        GCD = greatest_common_divisor(first_number, second_number)
        print("Greatest common divisor: {0}".format(GCD))
        exit_loop_character = input("Continue? (y/n): ")
        while exit_loop_character != 'n' and exit_loop_character != 'y':
            print("Please enter 'y' or 'n' to continue.")
            exit_loop_character = input("Continue? (y/n): ")
        if exit_loop_character == 'n':
            print("Bye!")
            break


if __name__ == '__main__':
    main()
