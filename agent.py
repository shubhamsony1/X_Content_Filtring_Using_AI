from moderator import check_tweet

#  Memory
history = []

# Decision Agent
def decide_action(label):
    if label == "HARMFUL":
        return "BLOCK"
    return "ALLOW"

# Action Agent
def take_action(tweet, result, action):
    if action == "BLOCK":
        print("\n🚨 BLOCKED")
        print(f"Tweet: {tweet}")
        print(f"Reason: {result['reason']}")
    else:
        print("\n✅ ALLOWED")


# Memory Agent
def store_memory(tweet, result, action):
    history.append({
        "tweet": tweet,
        "label": result["label"],
        "action": action
    })

# MAIN AGENT
def run_agent(tweet_text):
    # THINK
    result = check_tweet(tweet_text)

    # DECIDE
    action = decide_action(result["label"])

    # ACT
    take_action(tweet_text, result, action)

    # REMEMBER
    store_memory(tweet_text, result, action)

    return {
        "tweet": tweet_text,
        "label": result["label"],
        "reason": result["reason"],
        "action": action
    }