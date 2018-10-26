import praw

class Bot(object):
    def __init__(self, name):
        self.name=name 
        print(self.name)
        self.bot_connect = praw.Reddit(name)

    def read_subreddit(self, subreddit_name):
        if subreddit_name is None:
            print('subreddit name not found')
            return 
            # raise Exception

        self.content = self.bot_connect.subreddit(subreddit_name)
        
    def print_subreddit_content(self):
        for submission in self.content.hot(limit=5):
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("Score: ", submission.score)
            print("------------------------------------\n")

to_read = 'all' # input("please enter subreddit to read: ")
bot1 = Bot(name='bot1')
bot1.read_subreddit(to_read)
bot1.print_subreddit_content()