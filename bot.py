import requests
from bs4 import BeautifulSoup

URL = 'https://blocks.smileyco.in/address/BCTEdExMEL7WWFNbPtpQ8KfAqSsU3UDuM3'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='wrap')

#print(results.prettify())

job_elems = results.find_all('section', class_='container')

for job_elem in job_elems:
    print(job_elem, end='\n'*2)


print("DONE")
