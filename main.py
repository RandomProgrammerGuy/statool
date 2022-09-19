# Import "random" library #
from random import *
from termcolor import *

# -- S E L E C T   M O D E -- #
print("Select Mode:")                                                                                  # Print instructions on how to select mode
print("Type \"c\" to select mode coin throw or \"d\" to select mode dice throw")

mode = input()                                                                                         # Take mode input from user

if mode == "c" or mode == "C":                                                                         # Mode selector (+ Error if an ambigious mode is selected)
    print("Enter number of times you want to toss the coin")
    throw_numb = input()             
    coin_throw(throw_numb)
elif mode == "d" or mode == "D":
    print("Enter number of times you want to throw the dice")
    throw_numb = input()             
    dice_throw(throw_numb)
else: 
    print("Undefined mode selected. Program Terminated")

