# Argos
## Github notifier using `terminal-notifier`

Argos is an all-seeing 100-eyed Giant in Greek mythology, and also a python tool
for keeping track of your github notifications from the comfort of your desktop.

### Usage

1. install python 3
1. install pip
1. `pip install -r requirements.txt`
1. Create a file called `.api_token` with your username and a github API token
   you created using their interface, in the form of <name>:<token>
1. run `python notifier.py` and watch the nofifications roll in!


### Hacking

As you can see, it's an extremely simple tool - feel free to hack it to suit
your needs! For instance, you might want to make it filter only certain types of
notifications, or create a UI for perusing them on your machine. [The Github API
for notifications](https://developer.github.com/v3/activity/notifications/#list-your-notifications)
is pretty straightforward, so it's highly encouraged that you check out all the
various options you can pass to it!

