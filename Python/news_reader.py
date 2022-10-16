import json

import requests
from win32com.client import Dispatch  # pip install pywin32


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)  # produce voice


url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=e12f38df643a40e1971d6428d52de3ac"

r = requests.get(url)
cont = r.text
news = json.loads(cont)
# print(news)

articles = news["articles"]  # list of dictionaries of articles
# print(articles)

for article in articles:
    title = article["title"].split('-')
    print(title[0])  # prints Titles of news
    speak(title[0])

    print(article['description'])
    speak(article['description'])

    if article != articles[-1]:
        speak("Moving to next news...")
    else:
        pass

speak("Thankyou")
