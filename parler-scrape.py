import requests, sys, threading, time
from random import randint 
from itertools import islice
from csv import writer

#Scraping stuff
op_file = 'data/'

#log_file
log_file_thread = 'logs/thread.csv'
log_file_req = 'logs/requests.csv'

#Requests stuff
sesh = requests.session()

#Data file
ip_file = '40kf.csv'
users_left = True

#Threading stuff
lot = []
num_of_threads = 10
iters = 1

def posting(username, iters):

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
	'Cookie': '_pk_id.1.4eb6=c537e2ceea449bd0.1639087612.; _jsuid=962679935; _pk_ses.1.4eb6=1; _first_pageview=1; heatmaps_g2g_101336175=yes; PHPSESSID=72vu1ej2quuv9shl86umbsu3n5; parler_auth_token=d674d85888a0bbd5bb15f4defda2ee41540fdb5d748f8a6d0a9e635ead9bcf70',
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
		with open(log_file_req, 'r') as f:
			log_list = []
			log_list.append(username)
			log_list.append(r.elapsed.total_seconds())
			log_list.append(r.status_code)
			log_list.append(len(page))
			log_list.append(pg)
			log_list.append(iters)
			writer_obj = writer(f)
			writer_obj.writerow(log_list)

		if len(page) == 0:
			break
		pg += 1
		f = open(op_file+username+".json", "a+")
		json.dump(page,f,indent=1)
		f.close()

with open(ip_file, 'r') as f:
	users = []
	while users_left:
		print("Starting iter: %d\n"%iters)
		line = f.readline()
		if line:
			users.append(line.strip())
		elif len(users) == num_of_threads or not line:
			time_start_thread = time.time()

			for user in users:
				lot.append(threading.Thread(target=posting, args = (user,iters, )))
				lot[-1].start()

			for thread in lot:
				thread.join() 

			time_end_thread = time.time()

			delay = randint(2, 5)
			with open(log_file_thread,'r') as f:
				log_file_list = []
				log_file_list.append(str(iters))
				log_file_list.append(str(time_start_thread))
				log_file_list.append(str(time_end_thread))
				log_file_list.append(str(delay))

				writer_obj = writer(f)
				writer_obj.writerow(log_file_list)
				
			time.sleep(delay)
			if not line:
				users_left = False

			users = []
			iters += 1
