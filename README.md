# py-twitter-bot
A simple Python script to post a randomly selected tweet to a Twitter account.

The application utilizes Tweepy, a Python module for use with Twitter

## How to Use

- Download repository
- Install Python
- Install Tweepy `pip install tweepy`
- Modify **[credentials.py](https://github.com/alex-dulac/py-twitter-bot/blob/master/credentials.py)** with your **[Twitter Developer Credentials](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)**
- Populate **[content.txt](https://github.com/alex-dulac/py-twitter-bot/blob/master/content.txt)** with your tweets (One tweet per line)
- Run `python tweet.py` in your terminal

## How to schedule automatic executions

There are several ways this can be done. <br>
Personally, I schedule to run weekkly via a cron job. <br>
This can be done by doing the following: <br>

- Run `crontab -e` in your terminal.
- Populate the file as needed. Here is an example: `*/5 * * * * /usr/local/bin/python3 /<path_to_your_project>/tweet.py`
- The first part `*/5 * * * *` handles the timer. The example is scheduled to run every 5 minutes.
- The second part contains two paths: the first one points to the location of your python interpreter, and the second is the location of the file you want crontab to run at the specific time you set.
