import  requests
from collections import Counter
from pprint import pprint as pp

url = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"
json_obj = requests.get(url).json()

print "{"

#water point functioning
print "number_functional:"
c = Counter(player['water_functioning'] for player in json_obj)
c = dict(c)
pp(c)
print(c)

#Number of water points in total
print "number_water_points:"
c = Counter(player['water_pay'] for player in json_obj)
c = dict(c)
pp(c)
print(c)

#Number of water points per community_village
print "number_water_points_in_community:"
c = Counter(player['communities_villages'] for player in json_obj)
c = dict(c)
pp(c)
print(c)


#water point not functioning

f = filter(lambda x: x['water_functioning']!='yes', json_obj)
print "community_ranking;"
c = Counter(player['communities_villages'] for player in f)
c = dict(c)
pp(c)
print(c)

print "}"
