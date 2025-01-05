import tweepy
import time
import random

# Credenziali API (usa le variabili d'ambiente su Railway)
import os
api_key = os.getenv("API_KEY")
api_key_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Autenticazione con Tweepy
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Elenco di frasi casuali sulla mindfulness
mindfulness_quotes = [
    "Take a deep breath. Focus on the present moment. 🌿",
    "Mindfulness: the art of living fully in the here and now. 🕊️",
    "Pause, breathe, and let go of what doesn't serve you. 🌼",
    "Your mind is a garden. Nurture it with mindfulness. 🌷",
    "Inhale calm, exhale stress. Repeat. 🌸"
]

def publish_tweet():
    try:
        # Scegli una frase casuale
        tweet_content = random.choice(mindfulness_quotes)
        # Pubblica il tweet
        response = client.create_tweet(text=tweet_content)
        print(f"Tweet pubblicato con successo! ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print(f"Errore nella pubblicazione del tweet: {e}")

# Pubblica un tweet ogni mezz'ora
while True:
    publish_tweet()
    time.sleep(1800)  # 30 minuti
