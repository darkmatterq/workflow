import json

with open('stales.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

with open('new_state.json', 'w') as f:
    json.dump(data, f, indent=2)
