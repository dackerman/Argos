# Argos
## Github notifier using `terminal-notifier`

Argos is an all-seeing 100-eyed Giant in Greek mythology, and also a python tool
for keeping track of your github notifications from the comfort of your desktop.

### Usage

1. install python 3
1. install pip
1. `pip install -r requirements.txt`
1. Create a file called `.api_token` with your username and a github API token
   you created using their interface, in the form of `<name>:<token>`
1. run `python notifier.py` and watch the nofifications roll in!


### Hacking

As you can see, it's an extremely simple tool - feel free to hack it to suit
your needs! For instance, you might want to make it filter only certain types of
notifications, or create a UI for perusing them on your machine. [The Github API
for notifications](https://developer.github.com/v3/activity/notifications/#list-your-notifications)
is pretty straightforward, so it's highly encouraged that you check out all the
various options you can pass to it!

### License

```
Copyright (c) 2016 David Ackerman


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
