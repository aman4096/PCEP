import requests

year=2011
total=0
for i in range(11):
  URL = "https://jsonmock.hackerrank.com/api/football_matches"
  PARAMS = {'year':year,"team1goals":i,"team2goals":i}
  r = requests.get(url = URL, params = PARAMS)
  data = r.json()
  total=total+data['total']
  print (str(i) + " -> " + str(data['total']))  
print ("Total -> " + str(total))
