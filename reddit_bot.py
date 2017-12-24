import praw
import config
import time
import os

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "busterronitest's dog comment responder v0.1")

	return r

def run_bot(r, comments_replied):
	print("fetching 25 comments")
	print(comments_replied)

	for comment in r.subreddit('test').comments(limit=5):

		if "How to lose weight" in comment.body and comment.id not in comments_replied and comment.author != r.user.me():
			print("We found the key string")
			comment.reply("Calories in vs calories out is the important thing")

			with open ("cur_comments.txt", "a") as f:
				f.write(comment.id + "\n")
				print(type(comments_replied))
				comments_replied.append(comment.id)

	time.sleep(10)


def get_cur_comments():
	if not os.path.isfile("cur_comments.txt"):
		print("doesn't exist yet, lets make the txt file")
		comments_replied = []

	else:
		with open("cur_comments.txt", "r") as f:
			comments_replied = f.read()
			comments_replied = comments_replied.split("\n")
			comments_replied = list(filter(None, comments_replied))

	return comments_replied



r = bot_login()
comments_replied = get_cur_comments()

while True:
	run_bot(r, comments_replied)

