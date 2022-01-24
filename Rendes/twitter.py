#import tweepy
#auth = tweepy.OAuthHandler("xWaOHMW9GSNgjsr8ShNu3LO1R","0TgRFHwvwouqziWclqtISPWajliqoR0RjAwyNJmyfQUtjXd5gg")
#try:
#    redirect_url = auth.get_authorization_url()
#except tweepy.TweepError:
#    print('Error! Failed to get request token.')


import tweepy
import datetime
now=datetime.datetime.now()

auth = tweepy.OAuthHandler('xWaOHMW9GSNgjsr8ShNu3LO1R','0TgRFHwvwouqziWclqtISPWajliqoR0RjAwyNJmyfQUtjXd5gg')
auth.set_access_token('1450813593969123330-r1sSJVNPCUujRXbdNa6kbrQR9Iz3qJ','POBpiQTXpVU2UWKXOPuRHsi8dpUgWQKaHgOnktBGAdNsM')

ido=now.strftime("%H:%M:%S")

api = tweepy.API(auth)

api.update_status(str(ido))
print("sikeresen tweetelve az, hogy ", ido)
