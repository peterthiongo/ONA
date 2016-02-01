import  requests, json, ast
from collections import Counter,defaultdict
from pprint import pprint as pp

url = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"
json_obj = requests.get(url).json()

print "{"

#water point functioning
print "number_functional:"
c = Counter(player['water_functioning'] for player in json_obj)
c = dict(c)
print ast.literal_eval(json.dumps(c))

#Number of water points in total
print "number_water_points:"
c = Counter(player['water_pay'] for player in json_obj)
c = dict(c)
print ast.literal_eval(json.dumps(c))

#Number of water points per community_village
print "number_water_points_in_community:"
c = Counter(player['communities_villages'] for player in json_obj)
c = dict(c)
print ast.literal_eval(json.dumps(c))


#water point not functioning

communities = [j['communities_villages'] for j in json_obj]

#initialize data
data = defaultdict(float)
for community in communities:
    data[community]=0
#Count occurrances of a single community as a counter dictionary
counters = Counter((i['communities_villages'] for i in json_obj))

#Do the calculation
for i in json_obj:
    if i['water_functioning']== 'yes':
        inc = (counters[i['communities_villages']]*100)/len(json_obj)
        data[i['communities_villages']]+= float(inc)
    elif i['water_functioning']== 'no':
        dec = (counters[i['communities_villages']]*100)/len(json_obj)
        data[i['communities_villages']]-=float(dec)

print ast.literal_eval(json.dumps("community_ranking:"))


print {k:"{0}%".format(v) for k,v in data.items()}

print "}"
