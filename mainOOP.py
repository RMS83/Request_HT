from pprint import pprint
import requests

class Character:
    name_intelligence = {}

    def __init__(self, name):
        self.name = name
        url = f'https://superheroapi.com/api/2619421814940190/search/{self.name}'
        respo = requests.get(url)
        self.full_name = respo.json()['results'][0]['biography']['full-name']
        self.power = int(respo.json()['results'][0]['powerstats']['power'])
        self.combat = int(respo.json()['results'][0]['powerstats']['combat'])
        self.durability = int(respo.json()['results'][0]['powerstats']['durability'])
        self.intelligence = int(respo.json()['results'][0]['powerstats']['intelligence'])
        self.speed = int(respo.json()['results'][0]['powerstats']['speed'])
        self.strength = int(respo.json()['results'][0]['powerstats']['strength'])
        if self.intelligence not in self.name_intelligence.keys():
            self.name_intelligence[self.intelligence] = [self.name]
        else:
            self.name_intelligence[self.intelligence] += [self.name]

    def __str__(self):
      return f'Герой: {self.name}\nПолное имя: {self.full_name}' \
             f'\nСила: {self.power}\nБой: {self.combat}\nСтойкость: {self.durability}' \
             f'\nИнтеллект: {self.intelligence}\nСкорость: {self.speed}\nПрочность: {self.speed}'


def best_intelligent(dict_= Character.name_intelligence):
    best_intelligent = max(dict_.items())
    return f'Самый умный супергерой: {", ".join(best_intelligent[1])}'


if __name__ == '__main__':
    # hero = Character('Thanos')
    hero1 = Character('Hulk')
    hero2 = Character('Captain America')
    hero3 = Character('Dr Manhattan')

    # print(Character.name_intelligence)
    print(best_intelligent())
    # print(hero)





