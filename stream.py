import os
import tweepy
from dotenv import load_dotenv
from agent import run_agent

load_dotenv()


def fetch_tweets(client, query):
    response = client.search_recent_tweets(
        query=query,
        max_results=10,
        tweet_fields=["text", "author_id"],
        expansions=["author_id"],
        user_fields=["username"]
    )

    if not response.data:
        print("No tweets found.")
        return

    users = {}
    if response.includes and "users" in response.includes:
        for u in response.includes["users"]:
            users[u.id] = u.username

    for tweet in response.data:
        text = tweet.text

        if text.startswith("RT "):
            continue

        result = run_agent(text)

        username = users.get(tweet.author_id, "unknown")
        link = f"https://x.com/{username}/status/{tweet.id}"

        print("\n" + "="*50)
        print(f"User  : @{username}")
        print(f"Tweet : {text}")
        print(f"Label : {result['label']}")
        print(f"Action: {result['action']}")
        print(f"Link  : {link}")
        print("="*50)


def main():
    token = os.getenv("X_BEARER_TOKEN")

    if not token:
        print("Missing token")
        return

    client = tweepy.Client(bearer_token=token)

    query = "hate OR abuse OR spam OR violence lang:en"

    while True:
        fetch_tweets(client, query)

        choice = input("q = next, e = exit: ")
        if choice == "e":
            break


if __name__ == "__main__":
    main()