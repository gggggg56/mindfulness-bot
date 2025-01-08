import tweepy
import requests
import schedule
import time
import json

# Credenziali API di Twitter (le tue chiavi)
API_KEY = "9WaDv4BeWVekHNnKPb4syLqIG"
API_SECRET_KEY = "gHBQ5kwIYe9o7X2ywR6kc2jvYXagieSsDuU5xAMBfpKjwdNTEw"
ACCESS_TOKEN = "1623440224981250048-sndIrJoZ5tdZ2BqHPdC0D08TGHZItM"
ACCESS_TOKEN_SECRET = "s3zFl1B0joLWaPPegTqD6S3ghUZqWCRor5cnCrfofsPlM"

# Autenticazione con Twitter
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# URL dell'API ZenQuotes
QUOTE_API_URL = "https://zenquotes.io/api/random"

# File per salvare le citazioni pubblicate
PUBLISHED_QUOTES_FILE = "published_quotes.json"

# Carica le citazioni già pubblicate da file
def load_published_quotes():
    try:
        with open(PUBLISHED_QUOTES_FILE, 'r') as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

# Salva le citazioni pubblicate su file
def save_published_quotes(quotes):
    with open(PUBLISHED_QUOTES_FILE, 'w') as f:
        json.dump(list(quotes), f)

# Set per tracciare le citazioni pubblicate
published_quotes = load_published_quotes()

def fetch_random_quote():
    """Recupera una citazione casuale da ZenQuotes."""
    try:
        response = requests.get(QUOTE_API_URL)
        if response.status_code == 200:
            quote_data = response.json()
            # Estrarre il testo e l'autore della citazione
            quote_text = quote_data[0]['q']
            quote_author = quote_data[0]['a']
            return f"{quote_text} - {quote_author}"
        else:
            print("Errore nell'API per le citazioni.")
            return None
    except Exception as e:
        print(f"Errore durante il recupero della citazione: {e}")
        return None

def publish_tweet():
    """Pubblica un tweet con una citazione casuale."""
    try:
        # Recupera una citazione casuale
        tweet_content = fetch_random_quote()
        if tweet_content and tweet_content not in published_quotes:
            # Pubblica il tweet
            response = client.create_tweet(text=tweet_content)
            print(f"Tweet pubblicato: {response.data['id']}")
            # Aggiungi la citazione pubblicata al set
            published_quotes.add(tweet_content)
            # Salva le citazioni pubblicate su file
            save_published_quotes(published_quotes)
        else:
            print("Citazione duplicata o non valida. Saltato.")
    except tweepy.TweepyException as e:
        print(f"Errore nella pubblicazione del tweet: {e}")

# Pianifica i tweet al mattino e alla sera
schedule.every().day.at("08:00").do(publish_tweet)  # Mattino
schedule.every().day.at("20:00").do(publish_tweet)  # Sera

print("Bot avviato. In attesa di pubblicare i tweet...")

# Loop infinito per mantenere il programma in esecuzione
while True:
    schedule.run_pending()
    time.sleep(60)
