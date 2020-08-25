from popup import popup_window
import requests
import argparse
import tkinter as tk

# parser = argparse.ArgumentParser(description="RedditBot for subreddits")
# parser.add_argument("--subreddit", dest=)


SUB_REDDIT = "AskReddit"

RED_URL = f"https://www.reddit.com/r/{SUB_REDDIT}/new/.json?limit=50"

LOOK_QUES = ["What is", "What will", "What are"]

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}

req = requests.get(RED_URL, headers=headers)

if req.status_code == 200:
    req = req.json()
    data = req["data"]
    data = data["children"]

    for post in data:
        print(post["data"]["title"])
        title = post["data"]["title"]
        link = post["data"]["permalink"]
        for q in LOOK_QUES:
            if q in title:
                popup_window(title, link)

