import requests


r = requests.get('https://randomuser.me/api/?password=upper,lower,1-16')
data=r.json()
result=data['results'][0]
password=result['password']
print(password)
