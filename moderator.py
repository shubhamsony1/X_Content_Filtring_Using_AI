import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def check_tweet(tweet_text: str) -> dict:
    """
    Send a tweet to Claude and get a moderation decision.
    Returns a dict with keys: label, reason
    """
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=100,
        temperature=0,
        messages=[
            {
                "role": "user",
            "content": f"""
You are a strict content moderation system.

Classify the tweet into ONLY one of these:
SAFE
HARMFUL

Rules:
- HARMFUL includes hate speech, abuse, harassment, threats, or spam
- SAFE is normal, harmless content

Output format (STRICT):
SAFE: <short reason>
OR
HARMFUL: <short reason>

Do not add anything else.

Tweet: {tweet_text}
"""

            }
        ]
    )

    raw = response.content[0].text.strip()

    # Parse "SAFE: reason" or "HARMFUL: reason"
    raw = raw.strip()

    # Default fallback
    label = "SAFE"
    reason = "Could not determine clearly"

    upper = raw.upper()

    # Detect label safely
    if upper.startswith("HARMFUL"):
        label = "HARMFUL"
    elif upper.startswith("SAFE"):
        label = "SAFE"

    # Extract reason safely
    if ":" in raw:
        reason = raw.split(":", 1)[1].strip()
    else:
        reason = raw

    return {
        "label": label,
        "reason": reason,
        "tweet": tweet_text
    }


if __name__ == "__main__":
    # Quick test, run this file directly to try it out
    test_tweets = [
        "Just had a great cup of tea this morning!",
        "I hate everyone who supports that team, they should all suffer.",
        "Buy cheap followers now!! Click here for free likes!!!",
    ]

    for tweet in test_tweets:
        result = check_tweet(tweet)
        print(f"\nTweet : {result['tweet']}")
        print(f"Label : {result['label']}")
        print(f"Reason: {result['reason']}")





import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    raise ValueError("❌ Missing ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=API_KEY)


def check_tweet(tweet_text: str) -> dict:
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=100,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are a strict content moderation system.

Classify the tweet into ONLY one of these:
SAFE
HARMFUL

Rules:
- HARMFUL includes hate speech, abuse, harassment, threats, or spam
- SAFE is normal, harmless content

Output format (STRICT):
SAFE: <short reason>
OR
HARMFUL: <short reason>

Do not add anything else.

Tweet: {tweet_text}
"""
                }
            ]
        )

        raw = response.content[0].text.strip()

    except Exception as e:
        return {
            "label": "SAFE",
            "reason": f"API Error: {str(e)}",
            "tweet": tweet_text
        }

    label = "SAFE"
    reason = "Unknown"

    upper = raw.upper()

    if upper.startswith("HARMFUL"):
        label = "HARMFUL"
    elif upper.startswith("SAFE"):
        label = "SAFE"

    if ":" in raw:
        reason = raw.split(":", 1)[1].strip()

    return {
        "label": label,
        "reason": reason,
        "tweet": tweet_text
    }