import requests, sys, threading, time
from random import randint 
from itertools import islice

#Scraping stuff
op_file = 'data/'

#log_file
log_file_thread = 'logs/thread.csv'

#Requests stuff
sesh = requests.session()

#Data file
ip_file = '40kf.csv'

#Threading stuff
lot = []
num_of_threads = 10
iter = 1

def posting(username):

	dt = {'page': '1',
		'user': ''}

	headers = {'Host': 'parler.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://parler.com/user/JimJordan',
	'Content-Length': '286',
	'Origin': 'https://parler.com',
	'Connection': 'keep-alive',
	'Cookie': '_pk_id.1.4eb6=c537e2ceea449bd0.1639087612.; _jsuid=962679935; _pk_ses.1.4eb6=1; heatmaps_g2g_101336175=no; PHPSESSID=umvps3gr1clq4606jcm0758v7t; parler_auth_token=fd5c2dbcc73bb3d5d44bc722fa830c2b791fa0ac8636c5d7cc3897d8b63772db',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'no-cors',
	'Sec-Fetch-Site': 'same-origin',
	'Cache-Control': 'max-age=0, no-cache',
	'Pragma': 'no-cache'}

	pg = 1
	dt['user'] = username

	while True:
		dt['page'] = str(pg)

		r = sesh.post('https://parler.com/pages/feed.php', data = dt, headers = headers)

		page = r.json()
		
		if len(page) == 0:
			break
		pg += 1

with open(ip_file, 'r') as f:
	users = islice(f, 10)

	time_start_thread = time.time()

	for user in users:
		#lot.append(threading.Thread(target=posting, args = (user,)))
		#lot[-1].start()
		print(user)

	""" for thread in lot:
		thread.join() """

	time_end_thread = time.time()

	delay = randint(2, 5)
	""" with open(log_file_thread,'r') as f:
		log_file_list = []
		log_file_list.append(time_start_thread)
		log_file_list.append(time_end_thread) """

	#time.sleep(delay)
