"""
===================   TASK 1   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You can use `rand` module to simulate dice
* rolling.
===================================================
"""
from random import randrange
n = abs(int(input("How many times should the dice be rolled? ")))

number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0

for i in range(n):
    number = randrange(1, 7)
    if number == 1:
        number1 += 1
    if number == 2:
        number2 += 1
    if number == 3:
        number3 += 1
    if number == 4:
        number4 += 1
    if number == 5:
        number5 += 1
    if number == 6:
        number6 += 1

print(" Number 1 appeared", number1, "times\n", "Number 2 appeared", number2, "times\n", "Number 3 appeared", number3, "times\n"
      " Number 4 appeared", number4, "times\n", "Number 5 appeared", number5, "times\n", "Number 6 appeared", number6, "times\n")


