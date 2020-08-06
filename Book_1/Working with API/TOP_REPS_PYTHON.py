import requests
from plotly.graph_objs import Bar
from plotly import offline


url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accepts' : 'application/vnd.github.v3+json' }
r=requests.get (url , headers=headers)
print (f" Status code : {r.status_code}")

response_dict=r.json()
print (f"Total reps: {len(response_dict)}")
print (response_dict.keys())
repo_dicts=response_dict['items']
repo_names, stars, labels = [], [], []
print (f"That's how many reps in items {len(repo_dicts)}")
repo_dick=repo_dicts[0]
print (f"\nKeys: {len(repo_dick)}")
#for key in sorted (repo_dick.keys()):
#  print (key)


for repo_dick in  (repo_dicts):
  #print (f"name: {repo_dick['name']}")
  #print (f"owner: {repo_dick['owner']['login']}")
  #print (f"owner: {repo_dick['stargazers_count']}")
  #print (f"owner: {repo_dick['html_url']}")
  #print (f"owner: {repo_dick['description']}")
  repo_names.append(repo_dick['name'])
  stars.append(repo_dick['stargazers_count'])
  owner= repo_dick['owner']['login']
  description=repo_dick['description']
  label= f"{owner} <br />{description}"
  labels.append(label)

data=[{
  'type': 'bar',
  'x': repo_names,
  'y':stars,
  'hovertext': labels,
  'marker':{
    'color' : 'rgb(60,100,200)', # цвет столбцов
    'line': {'width': 1.5, 'color': 'rgb(25,10,30)'} # граница 1.5 пикселя определенного цвета
  },
  'opacity': 0.6, # тут у нас прозрачность
}]
my_layout= {
  'titlefont': {'size': 28},
  'xaxis': {
    'title': "Repa",
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
  'yaxis': {
    'title' : "Stars",
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
}
fig = {'data': data, "layout" : my_layout}
offline.plot(fig, filename="pythonovskie_Repi.html")
