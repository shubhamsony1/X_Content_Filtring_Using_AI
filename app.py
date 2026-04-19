from flask import Flask, request, render_template_string
from agent import run_agent

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Tweet Moderator</title>
  <style>
    body { font-family: Arial; max-width: 600px; margin: 60px auto; }
    textarea { width: 100%; height: 100px; }
    button { margin-top: 10px; padding: 10px; }
    .SAFE { background: #d4edda; padding: 15px; }
    .HARMFUL { background: #f8d7da; padding: 15px; }
  </style>
</head>
<body>

<h2>Agentic Tweet Moderator</h2>

<form method="POST">
<textarea name="tweet">{{ tweet }}</textarea><br>
<button type="submit">Check</button>
</form>

{% if result %}
<div class="{{ result.label }}">
<strong>{{ result.label }} → {{ result.action }}</strong>
<p>{{ result.reason }}</p>
</div>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    tweet = ""

    if request.method == "POST":
        tweet = request.form.get("tweet")
        if tweet:
            result = run_agent(tweet)

    return render_template_string(PAGE, result=result, tweet=tweet)


if __name__ == "__main__":
    app.run(debug=True)