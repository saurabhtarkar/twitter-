#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "o2kWZ9srV0L7dM62gLNkFuAyO"
consumer_secret = "2gVk1TznO3fZzsj2e2V9wWlEPLVCvu3o6O3QXB0eEesXhqXNRe"
access_key = "612649339-mN9htQtCv6ESjKXDmNu28kN8K4ztrKlIbugOgqxS"
access_secret = "Z5fF7cDHAzNncGF62KvhkW2cRtQFKsXHVAz9yx6NSLoUf"

#method to get a user's last 100 tweets
def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want; twitter only allows 200 at once
	number_of_tweets = 100

	#get tweets
	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)

	#create array of tweet information: username, tweet id, date/time, text
	tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

	#write to a new csv file from the array of tweets
	print "writing to {0}_tweets.csv".format(username)
	with open("{0}_tweets.csv".format(username) , 'w+') as file:
		writer = csv.writer(file, delimiter='|')
		writer.writerows(tweets_for_csv)


#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print "Error: enter one username"

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)
