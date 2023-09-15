import tweepy
from requests_oauthlib import OAuth1Session
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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




def make_tweet_fn(text):
    # print("\n in make tweet fn \n")
    #print(text)
    response = oauth.post("https://api.twitter.com/2/tweets",json=text)
    return response.json()


def get_tweet_fn(params):
    print("\n in get tweet fn \n")
    print("the id is ", params)
    response = oauth.get(
    "https://api.twitter.com/2/tweets", params=params)
    return response.json()

def delete_tweet_fn(id:str):
    print("\n in delete tweet fn \n")
    print(id)
    response = oauth.delete("https://api.twitter.com/2/tweets/{}".format(id))
    return response.json()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tweet", methods=["POST"])
def create_tweet():
    text = str(request.data)
    content = text[7:len(text)-1]

    print(text)

    response = make_tweet_fn({'text':content})
    return response

@app.route("/get", methods=["GET"])
def get_tweet():
    tweetId = str(request.args.get("tweetId"))
    print(tweetId)
    response = get_tweet_fn({"id": tweetId,"tweet.fields": "created_at"})
    return response


@app.route("/delete", methods=["DELETE"])
def delete_tweet():
    tweetId = request.args.get("tweetId")
    response = delete_tweet_fn(tweetId)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234, debug=True)