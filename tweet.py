import tweepy
import random
from credentials import *


class TwitterBot:
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        self.api = api

    def execute_tweet_text(self):
        file = open("content.txt", "r")
        tweets = file.readlines()
        file.close()

        if not tweets:
            print("You don't have any tweets :( ")
            return

        random.shuffle(tweets)  # let's shake 'em up

        last_line = tweets[-1]  # grab the last line of the txt file
        del tweets[-1]  # remove it so it won't be tweeted again

        new_file = open("content.txt", "w")
        for tweet in tweets:
            new_file.write(tweet)
        new_file.close()

        char_limit = 200
        if len(last_line) > char_limit:
            print("This tweet is too long: " + last_line)
            return
        else:
            self.api.update_status(last_line)
            print("Tweet has been posted!")

    def execute_tweet_media(self):
        media = "video.mov"
        upload_result = self.api.media_upload(media)
        self.api.update_status(status="", media_ids=[upload_result.media_id_string])
        print("Tweet has been posted with media!")


bot = TwitterBot(key, key_secret, token, token_secret)

# bot.execute_tweet_text()
# bot.execute_tweet_media()
