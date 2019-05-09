
"""
===================   TASK 2  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def suma(list):
    length = len(list)

    if length == 1:
        return list[0]
    else:
        return sum(list[1:]) + list[0]


def main():
    list = [7, 13, 6, 7, 1, 3]
    print("The sum of the list elements is: " + str(suma(list)))
    pass


if __name__ == "__main__":
    main()
