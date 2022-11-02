# Req 1.1 Import Plotly functions
from plotly.graph_objs import Bar, Layout
from plotly import offline
#Req 1.2 Import Die class from die.py
from die import Die

# Req 2 Instantiate Die object. Create a D6.
die = Die()

# Requirement 3 Make some rolls, and store results in a list.
results = [] # Req 3.1
#Req 3.2
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
    
# Req 4 Analyze the results.
# Req 4.1 create array to hold results
frequencies = []
# Req 4.2 Loop through results and append to array
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Req 5. Visualize the results.
#Req 5.1 place x_values in variable
x_values = list(range(1, die.num_sides+1))
#Req 5.2 Place bar data into data array
data = [Bar(x=x_values, y=frequencies)]

#Req 6 Create labels
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)

#Req 7
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
