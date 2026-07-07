## Author: Lane Dorscher
## Date:  07/04/2026
## Course: CSD-325
## Assignment: 4.2
## Description:
#       Open the program with instructions on how to use the menu; Highs, Lows, or Exit.
#       When the program starts, allow the user to select whether they want to see the high temperatures or the low temperatures, or to exit.
#       When the user selects 'lows', they should see a graph, in blue, that reflects the lows for those dates.
#       Allow the program to loop until the user selects exit.
#       When the user exits, provide an exit message.
#       Use what elements you can from previous programs, perhaps including sys to help the exit process.
#       Document all your changes, and save as sitka_high_low_"<your initials>".py. Ex. sitka_high_low_mss.py to your module-4 directory.

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
def main():
    # open file and collect data
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and high temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)

    # Display program introduction
    print("Sitka Weather Data: 2018")
    print("Select an option from the menu choices below")
    menu_item_choices = [1,2,3]

    # Display Menu options
    while True:
        print("\n") # spacer
        print("Weather Menu:")
        print("1. High Temperatures")
        print("2. Low Temperatures")
        print("3. Exit")
        print("\n")

        choice = int(input("Enter your choice: "))
        if choice not in menu_item_choices:
            print("Please select an option from the menu choices below")
            continue
        elif choice == 1:
            plot_graph("Daily High Temperatures - 2018", highs, 'red')
        elif choice == 2:
            plot_graph("Daily Low Temperatures - 2018", lows, 'blue')
        elif choice == 3:
            print("Thank you for using this program")
            sys.exit()
        else:
            print("Please select an option from the menu choices below")

def plot_graph(title, temp, color):
    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temp, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

if __name__ == "__main__":
    main()