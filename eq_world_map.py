# Req 1. Import libraries
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Req #2 Explore the structure of the data.
#Req 2.1 json and file path
filename = 'data/eq_data_30_day_m1.json'
#Req 2.2 Open file
with open(filename) as f:
    # Req 2.3 Load json data
    all_eq_data = json.load(f)
# Req 2.4 load all featres into dictionary
all_eq_dicts = all_eq_data['features']
#Req 3 Extract location data
#3.1 Create arrays
mags, lons, lats, hover_texts = [], [], [], []
#Req 3.2 place dicationaries in its own dicationary type
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    #Req 3.3 Add dictionaries to arrays
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    #Req3.4 add hover texts to array
    hover_texts.append(title)

#Req 4 Map the earthquakes.
data = [{
    #Req 4.1
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    #Req 4.2
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
#Req 5. Set Title
my_layout = Layout(title='Global Earthquakes')
#Req 6 Add dta and title to the figure
fig = {'data': data, 'layout': my_layout }
#Req 7 Set the plot to a  webpage
offline.plot(fig, filename='global_earthquakes.html')
