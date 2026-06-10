"""
Name: Lane Dorscher
Date: 6/10/2026
Assignment: Module 1.3 - 100 Bottles of Beer Countdown Program

Purpose:
This program asks the user for a starting number of bottles of beer and then
runs a countdown function that prints the lyrics of the "100 Bottles of Beer
on the Wall" song until it reaches zero.
"""


def main() -> int:

    numOfBottles = input("Enter number of bottles: ").strip()
    countdown(numOfBottles)
    print("\nTime to buy more bottles of beer.\n\n")
    return 0

def countdown(numOfBottles):

    counter = int(numOfBottles)
    while (counter > 0):
        print()
        if counter > 1:
            print(str(counter) + " bottles of beer on the wall, " + str(counter) + " bottles of beer!")
        else:
            print(str(counter) + " bottle of beer on the wall, " + str(counter) + " bottle of beer!")
        counter -= 1    
        print("Take one down and pass it around, " + str(counter) + " bottle(s) of beer on the wall.")

if __name__ == "__main__":
    main()