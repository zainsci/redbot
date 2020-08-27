from popup import popup_window
import requests
import argparse


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
            f"https://www.reddit.com/r/{args.sub}/{args.time}/.json", headers=headers, params=params)
        if req.status_code == 200:
            req = req.json()
            response = req["data"]["children"]
            return response

    else:
        req = requests.get(
            f"https://www.reddit.com/r/{args.sub}/.json", headers=headers)
        if req.status_code == 200:
            req = req.json()
            response = req["data"]["children"]
            return response


def parse_req(response, keyword, flare):
    if len(response) <= 0:
        print("No response")
        return

    elif flare:
        for post in response:
            if flare == post["data"]["link_flair_text"]:
                title = post["data"]["title"]
                link = post["data"]["permalink"]

                popup_window(title, link)

    elif keyword == None:
        for post in response:
            title = post["data"]["title"]
            link = post["data"]["permalink"]

            for q in QUESTIONS:
                if q in title:
                    popup_window(title, link)

    else:
        for post in response:
            title = post["data"]["title"]
            link = post["data"]["permalink"]
            print(title)

            if keyword in title:
                popup_window(title, link)


def main():
    parser = argparse.ArgumentParser(description="RedditBot for subreddits")
    parser.add_argument("--sub", type=str, default=None,
                        help="SubReddit to search for")
    parser.add_argument("--limit", type=int, default=None,
                        help="No of posts to search through at a time")
    parser.add_argument("--time", type=str, default=None,
                        help="Hot, New, Top or Rising posts")
    parser.add_argument("--keyword", type=str, default=None,
                        help="Any specific keyword to search for")
    parser.add_argument("--flare", type=str, default=None,
                        help="Falre to lookup for")
    args = parser.parse_args()

    response = make_request(args)
    parse_req(response, args.keyword, args.flare)


if __name__ == "__main__":
    main()
