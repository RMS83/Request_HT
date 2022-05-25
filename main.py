import json
from pprint import pprint

import requests

HERO = ['Thanos', 'Hulk', 'Captain America', 'Firebird', 'Atlas', 'Black Manta', 'Dr Manhattan']

def best_hero(heroes = HERO):
    hero_dict = {}
    for hero in heroes:
        url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        resp = requests.get(url).json()
        intelligence = int(resp['results'][0]['powerstats']['intelligence'])
        name = resp['results'][0]['name']
        if intelligence in hero_dict:
            hero_dict[intelligence] += [name]
        else:
            hero_dict[intelligence] = [name]
    key_val = max(hero_dict.items())
    print(hero_dict)
    return f'Самый умный супергерой: {"".join(key_val[1])}'

if __name__ == '__main__':
    print(best_hero())