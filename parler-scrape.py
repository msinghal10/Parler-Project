import requests, sys, threading, time

#Scraping stuff
op_file = 'data/'
#log_file
log_file = 'logs/'
#Requests stuff
sesh = requests.session()

#Threading stuff
lot = []

def posting(username):

	dt = '''-----------------------------5168501532397187871124942904
	Content-Disposition: form-data; name="page"

	1
	-----------------------------5168501532397187871124942904
	Content-Disposition: form-data; name="user"

	%s
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
	'Cookie': '_pk_id.1.4eb6=c537e2ceea449bd0.1639087612.; _jsuid=962679935; _pk_ses.1.4eb6=1; PHPSESSID=1h8pri4ksgrf7lk3ebjgrm6adm; parler_auth_token=fb2e52de155b391cd514c439b9c2610e7e22f601677c536c937a5ba8b230725a; _first_pageview=1; heatmaps_g2g_101336175=no', #Add cookies from browser 
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'no-cors',
	'Sec-Fetch-Site': 'same-origin',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache'}

	r = sesh.post('https://parler.com/pages/feed.php', data = dt%username, headers = headers)
	page = r.text 
	f = open(op_file+username, "w+")
	f.write(page)
	f.close()

print("Calling post")
posting("LightsOfLiberty")
	
""" time_now = time.time()

for x in range(100):
	lot.append(threading.Thread(target=posting))
	lot[x].start()

for x in lot:
	x.join()

time_after = time.time() 

print(time_after-time_now)"""