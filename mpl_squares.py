import matplotlib.pyplot as plt

#Req 1 Create the values for the squres
#1.1 Place the input values in variable named input_values
input_values = [1, 2, 3, 4, 5]
#1.2 Place the value of the squares in variable named squares
squares = [1, 4, 9, 16, 25]

#Req 2.1 Add the seaborn style to the plot
plt.style.use('seaborn')
# Req 2.2 Add the values to the plot and define the width of the line
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#Req 3 Set chart title and label axes.
#Req 3.1 Set the Title of the Figure and font size
ax.set_title("Square Numbers", fontsize=24)
#Req 3.2 Set the x value label
ax.set_xlabel("Value", fontsize=14)
# Req 3.3 Set the y value label
ax.set_ylabel("Square of Value", fontsize=14)

#Req 3.4 Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Req 4
plt.show()
