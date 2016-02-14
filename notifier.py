from pync import Notifier
from time import sleep

import requests
import datetime
import sys

github_auth = None
try:
    f = open('.api_token', 'r')
    username, token = f.readline().split(':')
    github_auth = (username, token)
except FileNotFoundError as e:
    print("Error: No .api_token file found. Create a github API token on their website, and put <username>:<token> in a file called .api_token in the current directory.")
    sys.exit()

wait = 70

def last_checked():
    try:
        with open('.last_checked', 'r') as f:
            return f.readline()
    except FileNotFoundError as e:
        return None

def update_last_checked(val):
    with open('.last_checked','w') as f:
        f.write(val)
    
def notify(notification):
    repo_url = notification['subject']['url']
    reason = notification['reason']
    title = notification['subject']['title']
    not_type = notification['subject']['type']
    
    r2 = requests.get(repo_url, auth=github_auth)
    repo = r2.json()
        
    url = repo['html_url']
    message = reason + ' ' + title
    Notifier.notify(message, title=not_type, open=url)


def getNotifications(last_checked):
    path = 'https://api.github.com/notifications'
    if last_checked:
        path = path + '?since=' + last_checked
    print("Calling {}".format(path))
    r = requests.get(path, auth=github_auth)
    notifications = r.json()
    print("found {} notifications".format(len(notifications)))

    for notification in notifications:
        notify(notification)

while True:
    getNotifications(last_checked())
    update_last_checked(datetime.datetime.now().isoformat())
    print('Waiting for {} seconds'.format(wait))
    sleep(wait)
