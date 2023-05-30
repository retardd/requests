import requests
import json

json_dict = json.loads(r.content)
hero_dict = {}

r = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')

for hero in json_dict:
    if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
        hero_dict[hero['name']] = hero['powerstats']['intelligence']

sort_list = [k for k in sorted(hero_dict, key=hero_dict.get, reverse=True)]
print(sort_list[0])