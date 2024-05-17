import openai
import tweepy
import os
from tweepy import Client

#setup openai
openai.api_key = os.getenv("OPENAI_API_KEY")
# setup twitter
api_key = os.getenv("INSERT API KEY")
api_secret = os.getenv("INSERT API KEY SECRET")
bearer_token = os.getenv("INSERT BEARER TOKEN")
access_token = os.getenv("INSERT ACCESS TOKEN")
access_token_secret = os.getenv("INSERT ACCESS TOKEN SECRET")

client = Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

commitMessage = os.getenv("COMMIT_MESSAGE")
prompt = f"Please create a summary of the following commit message: {commitMessage} and make sure it is clear and concise with a sense of wit. Make this a tweet for the perpuse of building in public."

def main():
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    tweet = response.choices[0].text
    api.update_status(tweet)





