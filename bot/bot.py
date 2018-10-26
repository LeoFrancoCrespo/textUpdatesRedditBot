import praw

class Bot(object):
    def __init__(self, *args, **kwargs):
        self.name=name 
        self.reddit_bot = praw.Reddit(name)

    def read_subreddit(subreedit_name):
        if subreddit_name is None:
            raise Exception

        content = self.reddit_bot
        print_subreddit_content(content)

        def print_subreddit_content(content):
            for submission in subreddit_content.hot(limit=5):
                print("Title: ", submission.title)
                print("Text: ", submission.selftext)
                print("Score: ", submission.score)
                print("------------------------------------\n")

to_read = input("please type a subreddit to read: ")
read_subreddit(to_read)