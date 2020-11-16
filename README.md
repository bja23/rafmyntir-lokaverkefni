Rafmyntir Haust 2020.
Lokaverkefni.
Björgvin Júlíus Ásgeirsson.
bja23@hi.is

Inngangur: Verkefnið snýst um að útbúa twitterbot. Hann á að sækja upplysingar um Smileycoin addressu og tweeta uppfærslum á henni.

Meiginmál: Byrjað var að útbúa plan. Fyrsta hugmyndin var að elta: https://blocks.smileyco.in/address/BCTEdExMEL7WWFNbPtpQ8KfAqSsU3UDuM3 og sækja upplýsingar í gegnum síðuna með svokölluðu web-scraping. Pælingin var að nota python og læra betur á það. Eftir mikla vinnu var leitast eftir öðrum bálkaskoðara þar se verkefnið var ekki að ganga vel. Fundin var annar bálkaskoðari: https://chainz.cryptoid.info/smly/address.dws?BCTEdExMEL7WWFNbPtpQ8KfAqSsU3UDuM3.htm og byrjað var á að reyna að ná upplýsingum frá henni. Við þá leit sást að sú síða biði upp á API. API var skoðaður og ákveðið að reyna að tengjast honum. Sótt var um lykil hjá Chainz.cryptoid þar sem þeir buðu upp á nákvæmari upplýsingar með lyklinum. Farið var í það ferli og fékkst lykilinn. Notast var við python og voru nauðsynlegir pakkar sóttir svo hægt væri að sækja upplýsingarnar. Notast var við pakkana: requests og BeautifulSoup til þess að sækja upplýsingarnar. Þeir voru sóttir með pip pakkastjórnara í gegnum terminal. Notast var við skipunirnar: getbalance og richrank til þess að fá stöðu um SMLY aura á addressu og í hvaða sæti á ríkalistanum sú addressa væri. Þegar þegar þetta heppnaðist var farið í að kynna sér tengingar við Twitter. Notast var við API kerfi hjá twitter. Útbúinn var twitter reikningur og sótt um developer leyfi á hann til þess að geta tengst honum í gegnum python. Þegar því ferli laug var farið að vinna í tenginum. Notast var við pakkann: tweepy, og var hann líka sóttur í gegnum pip pakkastjórann. Þegar á þennan stað var komið var útbúinn lykkja sem væri í gagni alltaf og þegar hún myndi finna breytingu á stöðu addressunar þá myndi forritið kanna stöðu á ríkalistanum svo myndi forritið enda á að tweeta um færsluna. Þar sem forritið keyrir stöðugt var ákvæðið að bregðast við tilmælum Chainz.cryptoid um að keyra ekki yfir síðuna þeirra. Ákveðið var að sækja pakkan: time og var auðvitað líka sóttur með pip pakkastjóranum. í lokinn var forritið keyrt yfir helgi til að kanna það og virkaði það vel. Forritið skrifaði 24 færslur á https://twitter.com/Bjrgvin19. Áður en forritinu var skilað, þá var kóðinn yfirfarinn og kommentaður einnig voru lykilorð fjarlægð.

Væntanlegar uppfærslur: Þar sem verkefnið var í skemmtilegri kanntinum er planið að halda áfram með það og uppfæra botann. Prófað hefur verið að vinna með skipunina: multiaddr og gefur hún upplýsingar um seinustu færslur á addressu. Hægt er að stilla hana með "n=10" og fengjust þá upplýsingar um seinustu 10 færslur. hér er linkurinn en lykilinn hefur verið fjarlægður.
https://chainz.cryptoid.info/smly/api.dws?q=multiaddr&active=BCTEdExMEL7WWFNbPtpQ8KfAqSsU3UDuM3&n=10&key=********


Upplýsingar um hvernig keyra eigi forritið.
1. Sækja þarf um developer leyfi á twitter og sækja consumer_key, consumer_secret, access_token og access_token_secret hjá þeim fyrir acc.
2. Sækja þarf um Key hjá https://chainz.cryptoid.info/api.key.dws.
3. Sækja bot.py skránna.
4. útbúa password file (vista hann á sama stað og bot.py) sem heitir password.py og í honum á að vera:
lykilord = ['consumer_key',
            'consumer_secret',
            'access_token',
            'access_token_secret',
            'key fyrir chainz.cryptoid'
            ]
4. sækja pakkana: requests, time, tweepy og BeautifulSoup
5. keyra með skipuninni: python3 bot.py


Lokaorð: Verkefnið var virkilega áhugavert og stal verkefnið algjörlega tímanum. Planið er að vinna með og uppfæra botann í jólafríinu. Verkefnið kenndi mér mikið og var gaman að kafa ofan í bálkaskoðarana. 
