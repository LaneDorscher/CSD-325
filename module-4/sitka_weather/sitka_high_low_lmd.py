## Author: Lane Dorscher
## Date:  07/04/2026
## Course: CSD-325
## Assignment: 4.2
## Description:
#       Program reads from a csv file containing daily weather data: humidity, high and low, etc.
#       User can request a plotted graph of the high or low temperatures

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
def main():
    """ main function, program entry point
    :return:
    """
    # open file and collect data
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and temperatures from this file.
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

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from the menu choices below")
            continue

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


def plot_graph(title, temp, color):
    """Function to plot the temperature graph
    Args: title - title of the graph, temp - array of temperature values, color - color of the graph
    """
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