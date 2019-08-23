import praw
import pandas as pd
from datetime import datetime

reddit = praw.Reddit(client_id='L35-VhD4_DcSCg', client_secret='Gv91Wq7gjPVZffa_9HEm-cL24dg', user_agent='keywordscraper')

keyword = input('Enter Your Subreddit: ')

hot_posts = reddit.subreddit(keyword).hot(limit=50)

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created_utc": [], \
                "body":[]}

for submission in hot_posts:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created_utc"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return datetime.fromtimestamp(created)

_timestamp = topics_data["created_utc"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv('results.csv', index=False)


