# Phyllis Torres
# Weather in Rome
# Due Date: 10/13/16

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# This program creates a dictionary with the average monthly temperatures for Rome, Italy. A function is called
# to total these temperatures and then get the average to determine the yearly average temperature.
# Another function is called to compare the temps to the yearly average and add any temps higher than the average
# to a new dictionary.

# print title of program and name
print color.BOLD + '\nWeather in Rome...\n' + color.END
print('Phyllis Torres\n')

print('This program calculates the yearly average temperature from monthly temperature data for Rome, Italy. ')
print('Each monthly temperature will then be compared to the yearly average. If the monthly temperature ')
print('is greater than the yearly average, it will be added to a new dictionary and printed out.\n\n')
# define global variables / dictionary
avgTemp = 0
hightemp = dict()

# create dictionary of average monthly temperatures for Rome, Italy
monthlyTemps = {'January': 54, 'February': 57, 'March': 61, 'April': 67, 'May': 75, 'June': 82, 'July': 88,
                'August': 88, 'September': 82, 'October': 73,
                'November': 62, 'December': 55}

# this function will calculate the average yearly temperature for Rome Italy
# the monthlyTemps dictionary is used as input
# the temps are accumulated in the total variable and then divided by the number of pairs in the dictionary
def avg_temp(d):
    total = 0
    global avgTemp
    for key in d:
        total = total + d[key]
    avgTemp = total / len(monthlyTemps)
    print('The average yearly temperature in Rome, Italy is: '),
    print str(avgTemp)

# this function will compare the temperatures in the monthlyTemps dictionary to the average yearly temperature
# calculated in he avg_temp(d) function. If the monthly temperature is greater than the average yearly
# temperature, it will be added to the hightemp dictionary. At the end of the function, the hightemp
# dictionary is printed out.
def highest_temp(d2):
    global avgTemp
    for key2 in d2:
        if d2[key2] > avgTemp:
            hightemp[key2] = (d2[key2])
    print('\nMonths where the temperatures are higher than the average temperature '
          'in Rome, Italy are: \n')
    print str(hightemp)

# Call the following functions using the monthlyTemps dictionary as the input parameter
avg_temp(monthlyTemps)
highest_temp(monthlyTemps)

# print out good bye in Italian
print('\nArrivederci!!!')

# print out the data source for the temperatures
print('\n\nData source: https://weather.com/weather/monthly/l/Rome+Italy+ITXX0067:1:IT')
