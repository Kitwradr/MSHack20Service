import json
import os

dirname = os.path.dirname(__file__)

stats = os.path.join(dirname, '../data/stats.json')
states = os.path.join(dirname, '../data/states.json')
stateWise = os.path.join(dirname, '../data/statewise.json')

with open(stats) as f:
    data_stats = json.load(f)

with open(states) as f:
    data_states = json.load(f)

hashed_states = dict()

for i in range(len(data_states)):
	hashed_states[data_states[i]['state']] = data_states[i]['name']

hashed_stats = dict()

for i in range(len(data_stats)):
	temp = dict()
	temp['positive'] = data_stats[i]['positive']
	temp['positiveIncrease'] = data_stats[i]['positiveIncrease']
	temp['totalTestsViral'] = data_stats[i]['totalTestsViral']
	temp['recovered'] = data_stats[i]['recovered']
	temp['death'] = data_stats[i]['death']
	temp['deathIncrease'] = data_stats[i]['deathIncrease']
	temp['state'] = data_stats[i]['state']
	hashed_stats[data_stats[i]['state']] = temp

for key in hashed_stats:
	hashed_stats[key]['name'] = hashed_states[key]

with open(stateWise, "w") as write_file:
	json.dump(list(hashed_stats.values()), write_file)
