# Import "random" library #
from cgi import print_form
import random

# -- COIN THROW FUNCTION -- #
def coin_throw():
    rand_i = random.randint(0, 1)
    outcomes = ["Heads", "Tails"]
    return outcomes[rand_i]

def dice_throw():
   return (random.randint(0, 9))

# -- S E L E C T   M O D E -- #
print("Select Mode:")                                                                                  # Print instructions on how to select mode
print("Type \"c\" to select mode coin throw or \"d\" to select mode dice throw")

mode = input()                                                                                         # Take mode input from user

i = 0                                                                                                  # Value for while loops
heads = 0
tails = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

if mode == "c" or mode == "C":                                                                         # Mode selector (+ Error if an ambigious mode is selected)
    print("Enter number of times you want to toss the coin")
    throw_numb = input()             
    while i < int(throw_numb):
        res = coin_throw()
        print(res)
        if res == "Heads":
            heads += 1
        else:
            tails += 1
        i += 1
    print("You got Heads " + str(heads) + " times and Tails " + str(tails) + " times")
    print("heads appeared " + str((heads/int(throw_numb)) * 100) + "\% of times and Tails " + str((tails/int(throw_numb)) * 100) + "\%")
elif mode == "d" or mode == "D":
    print("Enter number of times you want to throw the dice")
    throw_numb = input()             
    while i < int(throw_numb):
        res = dice_throw(throw_numb)
        print(res)
        if res == 1:
            one += 1
        elif res == 2:
            two += 1
        elif res == 3:
            three += 1
        elif res == 4:
            four += 1
        elif res == 5:
            five += 1
        else:
            six += 1
        i += 1
    print("1 appeared " + str(one) + " times, 2 appeared " + str(two) + " times, 3 appeared " + str(three) + " times, 4 appeared " + str(four) + " times, 5 appeared " + str(five) + " times and 6 appeared " + str(six) + " times")
    print("the percentage of 1s in the result was " + str(one/int(throw_numb)))
    print("the percentage of 2s in the result was " + str(two/int(throw_numb)))
    print("the percentage of 3s in the result was " + str(three/int(throw_numb)))
    print("the percentage of 4s in the result was " + str(four/int(throw_numb)))
    print("the percentage of 5s in the result was " + str(five/int(throw_numb)))
    print("the percentage of 6s in the result was " + str(six/int(throw_numb)))
else: 
    print("Undefined mode selected. Program Terminated")