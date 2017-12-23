import praw
import config
import time

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "busterronitest's dog comment responder v0.1")

	return r

def run_bot(r):
	for comment in r.subreddit('test').comments(limit=25):
		if "How to lose weight" in comment.body:
			comment.reply("Calories in vs calories out is the important thing")

	time.sleep(10)



r = bot_login()
while True:
	run_bot(r)

