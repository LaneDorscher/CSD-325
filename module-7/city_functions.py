## Author: Lane Dorscher
## Date:  07/22/2026
## Course: CSD-325
## Assignment: 7.2
## Description: Program formats the city, country, population and language and prints to the console

def city_country(city, country, population=None, language=None):
    output = city + ", " + country
    if population:
        output += " - population " + str(population)
    if language:
        output += ", " + language
    return output

print(city_country("New York", "United States"))
print(city_country("Paris", "France", 62300))
print(city_country("Santiago", "Chile", 5000000, "Spanish"))