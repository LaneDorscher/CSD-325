## Author: Lane Dorscher
## Date: 09/20/2025
## Description: This program calculates the cost of fiber optic cable installation based on user input.
##              The cost per foot varies depending on the total feet ordered,
##              allowing the user to save money when ordering in bulk.

## Edited Date: 6/19/2026
## Edited Note: Refactored code to use standardized naming convention

# Constants
COMPANY_NAME = "FibreTech"
WELCOME_MSG = f"Welcome to {COMPANY_NAME}'s Fiber Optic Cost Calculator!"
FEET_MESSAGE = "Feet of Fiber: "


# Functions
def get_float_input(prompt):
    '''
    Prompt the user to receive a valid floating point numeral.    
    :param prompt: Message to display to the user
    '''
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Must be a number!\n")


def get_cost_per_ft(feet):
    '''
    Returns the cost of the cable per feet granting discounts at business defined intervals.
    
    :param feet: 
    '''
    if feet >= 500.0:
        return 0.50
    elif feet >= 250.0:
        return 0.70
    elif feet >= 100.0:
        return 0.80
    else:
        return 0.87


# Main Code
def main():
    print(WELCOME_MSG)

    feet = get_float_input(FEET_MESSAGE)
    cost_per_ft = get_cost_per_ft(feet)
    total_cost = feet * cost_per_ft

    print(f"The cost per foot is: ${cost_per_ft:.2f}")
    print(f"The total cost for {feet} feet of fiber optics is: ${total_cost:.2f}")


if __name__ == "__main__":
    main()