#!/usr/bin/python3
'''Funcion que de manera recursiva, retorna una lista que contiene los titulos
de los articulos mas hot para un subreddit dado. En caso de que no se encuentre
nada, retorna none'''

import requests
import sys


def recurse(subreddit, hot_list=[]):
    '''Funcion'''
    i = 0
    subreddit = sys.argv[1]
    URL = 'http://reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    response = requests.get(URL, headers=headers).json()
    print(response['data']['children'][0]['data']['title'])