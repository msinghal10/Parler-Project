import requests, sys, threading, time


sesh = requests.session()


lot = []

dt = '''-----------------------------5168501532397187871124942904
Content-Disposition: form-data; name="page"

1
-----------------------------5168501532397187871124942904
Content-Disposition: form-data; name="user"

Lightsofliberty
-----------------------------5168501532397187871124942904--
'''

headers = {'Host': 'parler.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://parler.com/user/OANN',
'Content-Type': 'multipart/form-data; boundary=---------------------------5168501532397187871124942904',
'Content-Length': '282',
'Origin': 'https://parler.com',
'Connection': 'keep-alive',
'Cookie': '_pk_id.1.4eb6=c537e2ceea449bd0.1639087612.; _jsuid=962679935; _pk_ses.1.4eb6=1; heatmaps_g2g_101336175=no; PHPSESSID=94d2gne692jp2nmd4u7qbt8fg2; parler_auth_token=fee0a0373a46dd1e705e9c63bdbc7e5c4d7e9928c55ed99e5b48eb7c03a0295a; _first_pageview=1', #Add cookies from browser 
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Site': 'same-origin',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'}

def posting():
	r = sesh.post('https://parler.com/pages/feed.php', data = dt, headers = headers)
	# print(r.text)
time_now = time.time()

for x in range(100):
	lot.append(threading.Thread(target=posting))
	lot[x].start()

for x in lot:
	x.join()
time_after = time.time()

print(time_after-time_now)

# Cookie: _pk_id.1.4eb6=c537e2ceea449bd0.1639087612.; _jsuid=962679935; _pk_ses.1.4eb6=1; heatmaps_g2g_101336175=no; PHPSESSID=94d2gne692jp2nmd4u7qbt8fg2; parler_auth_token=fee0a0373a46dd1e705e9c63bdbc7e5c4d7e9928c55ed99e5b48eb7c03a0295a; _first_pageview=1