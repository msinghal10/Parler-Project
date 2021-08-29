import requests, sys
from bs4 import BeautifulSoup

sesh = requests.session()

payload = {
    "captcha_code": "ZjNb",
    "email": "kumarnihal15@yahoo.com",
    "password": "@Solvent5",
    "hash": "61f036c0-08da-9d1e-b6d5-ce7f3ba82df7",
    "device_id": "",
    "captcha_id": "53b420a0977016ca46c6f970242580c8d5a9c46a"
}

login = sesh.post('https://parler.com/functions/sessions/authentication/login/login.php', data = payload, )

f = open('asd.html', 'w')
data = login.text 
f.write(data)
f.close()

discover = sesh.get("https://parler.com/pages/feed.php?discover=true&page=1")
print(discover.status_code)
f = open('discover.html', 'w')
f.write(discover.text)
f.close()
sesh.close()