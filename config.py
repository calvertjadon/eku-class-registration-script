import json

with open('config.json', 'r') as f:
    config = json.loads(f.read())
    print(config)