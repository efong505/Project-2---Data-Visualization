# Req 1 Import libaries
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Req 2 Make an API call and store the response.
#REq 2.1 Store url in variable
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
#Req 2.2 Store response in variable
r = requests.get(url, headers=headers)
#Req 2.3 Print status code
print(f"Status code: {r.status_code}")

# Req 3 Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
# Req 4 Loop through data and append data to each array
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)


# Req 5 Make visualization of data.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

# Req 6 Style layout and graph items
my_layout = {
    # 'title': 'Most-Starred Ruby Projects on GitHub',
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}
# REq 7 Place data and layout into figure
fig = {'data': data, 'layout': my_layout}
#offline.plot(fig, filename='python_repos.html')
#Req 8 Plot data onto webpage
offline.plot(fig, filename='python_repos.html')
