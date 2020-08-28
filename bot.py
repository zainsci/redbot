from popup import notification
import requests
import argparse
from datetime import datetime
from time import sleep


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
QUESTIONS = ["What is", "What are", "What will"]


def make_request(args):
    if not args.sub:
        args.sub = "AskReddit"

    elif not args.limit:
        args.imit = 50

    if args.time:
        params = {
            "limit": args.limit,
        }
        req = requests.get(
            f"https://www.reddit.com/r/{args.sub}/{args.time}/.json",
            headers=headers,
            params=params,
        )
        if req.status_code == 200:
            req = req.json()
            response = req["data"]["children"]
            return response

    else:
        req = requests.get(
            f"https://www.reddit.com/r/{args.sub}/.json", headers=headers
        )
        if req.status_code == 200:
            req = req.json()
            response = req["data"]["children"]
            return response


def k_or_m(value):
    if int(value) > 1000000:
        value = int(value) / 1000000
        return str(value) + "M"
    elif int(value) > 1000:
        score = int(value) / 1000
        return str(value) + "K"
    else:
        return value


def convert_time(time):
    time = datetime.fromtimestamp(time).strftime("%H:%M")
    return time


def parse_req(response, keyword, flare, interval):
    if len(response) <= 0:
        print("No response")
        return

    elif flare:
        for post in response:
            if flare == post["data"]["link_flair_text"]:
                sub = post["data"]["subreddit"]
                title = post["data"]["title"]
                score = k_or_m(post["data"]["score"])
                comments = k_or_m(post["data"]["num_comments"])
                time = convert_time(post["data"]["created_utc"])
                link = post["data"]["permalink"]

                notification(sub, title, score, comments, time, link, interval)

    elif keyword:
        for post in response:
            sub = post["data"]["subreddit"]
            title = post["data"]["title"]
            score = k_or_m(post["data"]["score"])
            comments = k_or_m(post["data"]["num_comments"])
            time = convert_time(post["data"]["created_utc"])
            link = post["data"]["permalink"]

            if keyword in title.split():
                notification(sub, title, score, comments, time, link, interval)

    else:
        for post in response:
            sub = post["data"]["subreddit"]
            title = post["data"]["title"]
            score = k_or_m(post["data"]["score"])
            comments = k_or_m(post["data"]["num_comments"])
            time = convert_time(post["data"]["created_utc"])
            link = post["data"]["permalink"]

            for q in QUESTIONS:
                if q in title:
                    notification(sub, title, score, comments, time, link, interval)


def main():
    parser = argparse.ArgumentParser(description="RedditBot for subreddits")
    parser.add_argument("--sub", type=str, default=None, help="SubReddit to search for")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="No of posts to search through at a time",
    )
    parser.add_argument(
        "--time", type=str, default=None, help="Hot, New, Top or Rising posts"
    )
    parser.add_argument(
        "--keyword", type=str, default=None, help="Any specific keyword to search for"
    )
    parser.add_argument("--flare", type=str, default=None, help="Falre to lookup for")
    parser.add_argument(
        "--interval",
        type=int,
        default=None,
        help="Set timer between each post that appears",
    )
    args = parser.parse_args()

    response = make_request(args)
    parse_req(response, args.keyword, args.flare, args.interval)


if __name__ == "__main__":
    while True:
        main()
        sleep(600)
