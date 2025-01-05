import tweepy
import time
import random

# Credenziali API
API_KEY = "9WaDv4BeWVekHNnKPb4syLqIG"
API_SECRET_KEY = "gHBQ5kwIYe9o7X2ywR6kc2jvYXagieSsDuU5xAMBfpKjwdNTEw"
ACCESS_TOKEN = "1623440224981250048-sndIrJoZ5tdZ2BqHPdC0D08TGHZItM"
ACCESS_TOKEN_SECRET = "s3zFl1B0joLWaPPegTqD6S3ghUZqWCRor5cnCrfofsPlM"

# Autenticazione
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Elenco di frasi casuali sulla mindfulness
tweets_list = [
    "Take a moment to breathe deeply and reset your mind. 🌟 #Mindfulness",
    "Pause, reflect, and let go of stress. You're in control. 💫 #MindfulLiving",
    "Mindfulness is the key to unlocking inner peace. Take it one breath at a time. 🌿",
    "Remember, the present moment is all you truly have. Embrace it fully. 🌸 #Now",
    "Start your day with gratitude and mindfulness. It sets the tone for success. 🌅"
]

def publish_tweet():
    try:
        # Scegli una frase casuale
        tweet_content = random.choice(tweets_list)
        # Pubblica il tweet
        response = client.create_tweet(text=tweet_content)
        print(f"Tweet pubblicato con successo! ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print(f"Errore nella pubblicazione del tweet: {e}")

# Test iniziale
publish_tweet()

# Pubblica un tweet ogni 30 minuti
while True:
    time.sleep(1800)  # Pausa di 30 minuti (1800 secondi)
    publish_tweet()
