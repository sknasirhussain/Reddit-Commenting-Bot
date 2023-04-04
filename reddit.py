import praw
import config
import time
import os 


def login():
    print("logging in...")
    reddit = praw.Reddit(username = config.username, 
                        password = config.password,
                        client_id = config.client_id,
                        client_secret = config.client_Secret,
                        user_agent = "bot commenting v0.1")
    print("logged in.")
    return reddit



def run(reddit, replied_comments):

    print("obtainig 10 comments...")
    for comment in reddit.subreddit('test').comments(limit=10):

        if "dog" in comment.body and comment.id not in replied_comments and comment.author != reddit.user.me():

            print("Comments containg \"hello there\" found at " + comment.id)
            comment.reply("General Kenobi..!")

            print("replied to: " + comment.id)
            replied_comments.append(comment.id)

            with open("replied_Comments.txt", "a") as f:
                f.write(comment.id + "\n")

    print("sleeping for 10 secs cz reddit wont allow me T_T ...")
    print(replied_comments)

    time.sleep(10)


def get_saved_Comments():
    if not os.path.isfile("replied_comments.txt"):
        print("creating a new file...")
        replied_comments = []
        print("new file created!")

    else:   
        print("entering values to existing file...")  
        with open("replied_comments.txt", "r") as c:
            replied_comments = c.read
            replied_comments = replied_comments.split("\n")

    return replied_comments

reddit = login()
replied_comments = get_saved_Comments()
print(replied_comments)

while True:
    run(reddit, replied_comments)
