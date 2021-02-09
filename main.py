import requests
from pprint import pprint

r = requests.get('https://randomuser.me/api/?gender=female')
data=r.json()['results']
print(data)
#for i in data:
 #   print(i['gender'])