import sys
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

consumerKey = 'XPwfwwyoTNpmg5NcPKUO8M8ib'
consumerSecret = 'THShEsXn5JXO9ne1n2lyWziPaF0K8zAmRezzp2oUTwBMGBKd8p'
accessToken = '1093651106-PkZMj57hsHr8fesg0nOutRop4n9zlOBRuLayQ92'
accessTokenSecret = 'Xa8QhnqhMfU9q7sSdT7PruyMlLXfTiXMvpPc0mJ0vBEx2'

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

keyword = input("Ingrese palabra clave a buscar en los tweets: ")
nroTweets = int(input("Número de tweets a analizar: "))

tweets = tweepy.Cursor(api.search, keyword).items(nroTweets)

non_bmp_map = dict.fromkeys (range (0x10000, sys.maxunicode + 1), 0xfffd)
good = 0
bad = 0
neither = 0
polaridad = 0
sentimientos = 0

def percentage(marks, outof):
    per = marks*100/outof
    return per

for i in tweets:
    # print((i.text).decode('utf-8'))
    print((i.text).translate (non_bmp_map))
    print("\n")
    parametros = TextBlob((i.text).translate (non_bmp_map))
    var = parametros.sentiment.polarity
    sentimientos = sentimientos + var

    if(var == 0):
        neither = neither + 1
    elif (var > 0.00):
        good = good + 1
    elif (var < 0.0):
        bad = bad + 1

good = percentage(good, nroTweets)
bad = percentage(bad, nroTweets)
neither = percentage(neither, nroTweets)

print("Good:",good)
print("Bad:",bad)
print("Neither:",neither)
