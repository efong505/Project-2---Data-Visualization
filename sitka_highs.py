#Req 1 import libraries
import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Req 2 Open CSV File
#Req 2.1 Place filename and path in variable
filename = 'data/sitka_weather_2018_simple.csv'
#Req 2.2 Use open function to open file
with open(filename) as f:
    # Req 2.3 Reader object
    reader = csv.reader(f)
    header_row = next(reader)

    # Req #3 Get dates and high temperatures from this file.
    #Req 3.1 Create arrays for dates and highs
    dates, highs = [], []
    # Req 3.2 Loop through file and add dates and highs to arrays
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

# Req 4 Plot the high temperatures.
#Req 4.1 use seaborn style
plt.style.use('seaborn')
#Req 4.2 Create plot
fig, ax = plt.subplots()
# Req 4.3 Add dates and higs to plot
ax.plot(dates, highs, c='red')

# Req 5 Format plot.
#Req 5.1
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#Req 6 Show plot
plt.show()