import requests
import time
import tweepy
from bs4 import BeautifulSoup
from password import lykilord

#lykilord eru vistuð í password.py skrá í sömu möppu. skoða README
consumer_key = lykilord[0]
consumer_secret = lykilord[1]
access_token = lykilord[2]
access_token_secret = lykilord[3]
chain_crypto_key = lykilord[4]

# Betzy addressan
betzy = 'BEtZyyYqDXqmRJJ45nnL15cuASfiXg9Yik'
# Mín addressa.
MyURL = 'BCTEdExMEL7WWFNbPtpQ8KfAqSsU3UDuM3'

# Lykilbreytur
teljari = 0
igangi = True
riceList = ''
myBalance = ''
whereOnTheList = 'https://chainz.cryptoid.info/smly/api.dws?q=richrank&a=' + MyURL + '&key=' + chain_crypto_key
howsTheBalance = 'https://chainz.cryptoid.info/smly/api.dws?q=getbalance&a=' + MyURL + '&key=' + chain_crypto_key

# Fall til þess að tweeta. Fær inn streng og tweetar honum.
def tweeta(skilabod):
    def Tweetum():
        try:
            stadfesta = tweepy.OAuthHandler(consumer_key, consumer_secret)
            stadfesta.set_access_token(access_token, access_token_secret)
            return stadfesta
        except Exception as e:
            return None

    ostadfest = Tweetum()
    api = tweepy.API(ostadfest)
    api.update_status(skilabod)


# hér fáum við URL sent inn og sækjum texta þaðan.
def getList(listi):
    res = requests.get(listi)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    set([t.parent.name for t in text])
    # Ætlað fyrir næstu uppfærslu á botanum.
    sleppaordum = []
    list = ''
    for t in text:
        if t.parent.name not in sleppaordum:
            list += '{} '.format(t)
    newList = list
    return newList

# Þessi lykkja er stöðugt í keyrslu þar til að slökkt er á forriti.
while(igangi):
    # sótt uppfærslu á aurum.
    cash = getList(howsTheBalance)
    if(myBalance != cash):
        teljari = teljari + 1
        num = str(teljari)
        myBalance = cash
        # sótt stöðu á ríka listanum.
        temp = getList(whereOnTheList)
        # UPPFÆRSLA!!! Addressan: ... á ... SMLY. Add er í sætir
        skilabod_tweet = num +'. UPPFÆRSLA!!! Addressan: ' + MyURL + ' á: ' + myBalance + 'SMLY. Hún er í sæti: ' + temp + ' á ríka listanum. \n'
        print(skilabod_tweet)
        tweeta(skilabod_tweet)
    # forrit sett á sleep í 60 sek til þess að keyra ekki yfir Chainz.cryptoid
    time.sleep(60)


print("Slökkt")
