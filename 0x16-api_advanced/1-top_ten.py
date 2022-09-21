#!/usr/bin/python3
'''Funcion que printea los top 10 hot posts titulos listados para un
dado subreddit'''

import requests
import sys


def top_ten(subreddit):
    '''Function'''
    try:
        i = 0
        subreddit = sys.argv[1]
        URL = 'http://reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
        headers = {
            'User-Agent': 'My User Agent 1.0'
        }
        response = requests.get(URL, headers=headers).json()
        while i < 10:
            print(response['data']['children'][i]['data']['title'])
            i = i + 1
    except Exception as error:
        print("None")
