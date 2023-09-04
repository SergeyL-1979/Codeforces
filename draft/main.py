import os

import requests
import json

if not os.path.exists('data'):
    os.mkdir('data')


def get_gym():
    url = 'https://codeforces.com/api/contest.list?gym=true'
    response = requests.get(url=url).json()
    with open('data/gym.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


def get_problems():
    url = 'https://codeforces.com/api/problemset.problems'
    response = requests.get(url=url).json()
    with open('data/problems.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


def get_tasks():
    """ Сортировка по tags """
    url = 'https://codeforces.com/api/problemset.problems?tags=math;games'
    response = requests.get(url=url).json()
    with open('data/tags.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


def get_action():
    url = 'https://codeforces.com/api/recentActions?maxCount=30'
    response = requests.get(url=url).json()
    with open('data/action.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


def main():
    get_gym()
    # get_problems()
    # get_tasks()
    # get_action()


if __name__ == '__main__':
    main()
