import praw 

bot1='bot1'

def read_subreddit(subreddit):
    if subreddit is None:
        raise Exception
    
    subreddit_content = praw.Reddit('bot1').subreddit(subreddit)
    print_subreddit_content(subreddit_content)

def print_subreddit_content(subreddit_content):
    for submission in subreddit_content.hot(limit=5):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("------------------------------------\n")

to_read = input("please type a subreddit to read: ")
read_subreddit(to_read)