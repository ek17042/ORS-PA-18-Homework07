"""
===================   TASK 4  ====================
* Name: Number of Appearances
*
* Write a function that will return which element
* of integer list has the greatest number of
* appearances in that list.
* In case that multiple elements have the same
* number of appearances return any.
*
* Note: You are not allowed to use built-in
* functions.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def nr_of_app_in_list(lista):

    d = {}
    length = len(lista)
    nr_of_app = 0

    for i in range(length):

        if lista[i] not in d:

            for number in range(i, length):
                if lista[number] == lista[i]:

                    nr_of_app += 1

                given_number = lista[i]

                d[given_number] = nr_of_app
        nr_of_app = 0

    sequence = []

    for key in d:

        sequence.append(d[key])
    maximum = sequence[0]

    for i in range(len(sequence)):
        if sequence[i] > maximum:
            maximum = sequence[i]

    for key in d:
        if maximum == d[key]:
            return key


def main():

    lista = [3, 3, 2, 3, 6, 3, 3, 8, 3, 0, 9, 1, 2, 3, 3]
    x = nr_of_app_in_list(lista)

    print("In the given list number that appears the most is : " + str(x))
    pass


if __name__ == "__main__":
    main()
