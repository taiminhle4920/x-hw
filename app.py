import tweepy
from requests_oauthlib import OAuth1Session
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
user_name = "MinhTaiLe655422"
api_key = "tIFYnmON3Mr9PHGEXqtoksEgk"
api_secret = "w8VhfIFjClnjDNjWWf2s0n5OLvjidY49f2fPNBetaJXhQdvIkM"
bearer_token = "AAAAAAAAAAAAAAAAAAAAACSmpwEAAAAAbrfo%2FLMlGOVLUt64BCB2FjWBA5U%3DUGSeJUJENB3Tf13YmYFBXOsHUE9zGcTUgBOAwqmLFrDq9qhq4X"
access_token = "1701545563802808320-Hx17m6g6NrIWw1gaxpwXzPJmaif951"
access_token_secret = "789iXcwnjtD33VzYLJB6kwnPFGBSh5F1gfdUngqgv9c4F"



oauth = OAuth1Session(
    api_key,
    client_secret=api_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# code by Tai
def make_tweet_fn(text):
    response = oauth.post("https://api.twitter.com/2/tweets",json=text)
    return response.json()

# code by Tai

def delete_tweet_fn(id:str):
    response = oauth.delete("https://api.twitter.com/2/tweets/{}".format(id))
    if response.status_code == 400:
        return jsonify({"error":"tweetID not found"})
    elif response.status_code == 200:
        return jsonify({"success":"tweet deleted"})
    return response.json()

# code by Tai

@app.route("/")
def index():
    return render_template("index.html")

# code by Tai

@app.route("/tweet", methods=["POST"])
def create_tweet():
    text = str(request.data)
    content = text[7:len(text)-1]
    if len(content) == 0:
        return jsonify({"error":"content is empty"})
    response = make_tweet_fn({'text':content})
    return response

# code by Tai

@app.route("/delete", methods=["DELETE"])
def delete_tweet():
    tweetId = request.args.get("tweetId")
    if len(tweetId) == 0:
        return jsonify({"error":"tweetId is empty"})
    response = delete_tweet_fn(tweetId)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234, debug=True)
