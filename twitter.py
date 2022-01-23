#import tweepy
#auth = tweepy.OAuthHandler("xWaOHMW9GSNgjsr8ShNu3LO1R","0TgRFHwvwouqziWclqtISPWajliqoR0RjAwyNJmyfQUtjXd5gg")
#try:
#    redirect_url = auth.get_authorization_url()
#except tweepy.TweepError:
#    print('Error! Failed to get request token.')


import tweepy
import random

auth = tweepy.OAuthHandler('xWaOHMW9GSNgjsr8ShNu3LO1R','0TgRFHwvwouqziWclqtISPWajliqoR0RjAwyNJmyfQUtjXd5gg')
auth.set_access_token('1450813593969123330-r1sSJVNPCUujRXbdNa6kbrQR9Iz3qJ','POBpiQTXpVU2UWKXOPuRHsi8dpUgWQKaHgOnktBGAdNsM')

api = tweepy.API(auth)
randomszam = random.randrange(1,100)
api.update_status(str(randomszam))
print("sikeresen tweetelve az, hogy ", randomszam)
