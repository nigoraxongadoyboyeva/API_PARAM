import requests


r = requests.get('https://randomuser.me/api/?inc=gender,name,nat')
data=r.json()['results']
print(data)