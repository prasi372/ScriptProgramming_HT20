"""
This file contains a demo of function calls in Python
"""


# This function squares a given value
def squaring(x):
    return x ** 2


# This function cubes a given value
def cubing(x):
    return x ** 3


# Execution starts here
def main():
    numbers = [0, 1, 2, 3, 4, 5]

    for i in range(len(numbers)):
        # print("x={0}, x^2={1}, x^3={2}".format(i, squaring(i), cubing(i)))
        print("x={0}, x^2={1}, x^3={2}".format(numbers[i], squaring(numbers[i]), cubing(numbers[i])))


# If the script is executed, call main()
if __name__ == "__main__":
    main()
