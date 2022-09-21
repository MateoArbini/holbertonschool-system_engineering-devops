#!/usr/bin/python3
'''Function that returns the total amount of subscribers
including not active users, and total subscribers for
a given subreddit.'''

import requests
import sys


def number_of_subscribers(subreddit):
    '''Function'''
    try:
        subreddit = sys.argv[1]
        URL = 'http://reddit.com/r/{}/about.json'.format(subreddit)
        headers = {
            'User-Agent': 'My User Agent 1.0'
        }

        # Hago la request
        response = requests.get(URL, headers=headers).json()
        subscribers = response['data']['subscribers']
        return subscribers
    except Exception as error:
        return 0
