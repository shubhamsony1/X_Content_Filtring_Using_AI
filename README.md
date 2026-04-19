# Agentic Tweet Content Moderator

### AI-powered system to detect and act on harmful tweets using Claude AI

------------------------------------------------------------------------

## 🚀 Overview

This project is an **Agentic AI-based tweet moderation system** that
analyzes tweets from **X (Twitter)** and classifies them as:

-   SAFE\
-   HARMFUL

It implements a multi-agent pipeline: Observe → Think → Decide → Act →
Remember

------------------------------------------------------------------------

## 📂 Project Structure

project/ 
│
├── app.py 
├── stream.py 
├── agent.py 
├── moderator.py 
├──.env 
└──requirements.txt 

------------------------------------------------------------------------

## ⚙️ Features

-   AI-based tweet classification\
-   Agent-based decision system\
-   Real-time tweet monitoring\
-   Web UI (Flask)\
-   Memory of past moderation

------------------------------------------------------------------------

## 🛠️ Setup

### Install dependencies

pip install -r requirements.txt

### Add API keys (.env)

ANTHROPIC_API_KEY=your_key\
X_BEARER_TOKEN=your_token

------------------------------------------------------------------------

## ▶️ Run

### Web App

python app.py\
Open http://localhost:5000

### Stream Tweets

python stream.py

------------------------------------------------------------------------

## 🧪 Example

Input:\
"I hate everyone from that group"

Output:\
HARMFUL → BLOCK

------------------------------------------------------------------------

## 🧠 Tech Stack

Python, Flask, Claude AI, Tweepy

------------------------------------------------------------------------

## 📌 Note

-   Keep .env secret\
-   Claude API requires credits\
-   X API has limits

------------------------------------------------------------------------

## 🙌 Author

Shubham Sony
