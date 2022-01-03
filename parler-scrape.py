import requests, threading, time
from random import uniform
from csv import writer
import json	

#Scraping stuff
op_file = 'data/'
delay_lb = 0.1
delay_ub = 1
update_api = requests.session()

#log_file
log_file_req = 'logs/requests.csv'

#Requests stuff
sesh = requests.session()

#Data file
ip_file = '61k-101k.csv'
users_left = True

#Threading stuff
num_of_threads = 20
lot = [None] * num_of_threads
users_finished = 0

def posting(username, iters):

	more_than_one = False

	dt = {'page': '1',
		'user': ''}

	headers = {'Host': 'parler.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://parler.com/user/OANN',
	'Content-Length': '286',
	'Origin': 'https://parler.com',
	'Connection': 'keep-alive',
	'Cookie': 'PHPSESSID=0oo72sl4i5c8mh9o5t6lldu2mk; _pk_ref.1.4eb6=%5B%22%22%2C%22%22%2C1641176737%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.4eb6=3ff8d938311a192e.1641176737.; parler_auth_token=ccd5698fe59986249f55154564fb6a8df477f3d624f59309a8131bdd26cec684',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'no-cors',
	'Sec-Fetch-Site': 'same-origin',
	'Cache-Control': 'max-age=0, no-cache',
	'Pragma': 'no-cache'}

	pg = 1
	dt['user'] = username

	while True:
		dt['page'] = str(pg)

		delay=0
		
		if more_than_one:
			delay = uniform(delay_lb, delay_ub)
			time.sleep(delay)

		r = sesh.post('https://parler.com/pages/feed.php', data = dt, headers = headers)
		
		more_than_one = True

		page = r.json()
		with open(log_file_req, 'a+') as f:
			log_list = []
			log_list.append(username)
			log_list.append(str(r.elapsed.total_seconds()))
			log_list.append(str(r.status_code))
			log_list.append(str(pg))
			log_list.append(str(iters))
			log_list.append(str(delay))
			writer_obj = writer(f)
			writer_obj.writerow(log_list)

		if len(page) == 0:
			break
		pg += 1
		gf = open(op_file+username+".json", "a+")
		json.dump(page,gf,indent=1)
		gf.close()

with open(ip_file, 'r') as inp:
	
	for user in inp:
		user_assigned = False 
		while user_assigned == False:
			for i in range(num_of_threads):
				if lot[i] == None or lot[i].is_alive() == False:
					#Time to create a new thread
					lot[i] = threading.Thread(target=posting, args=(user.strip(), users_finished))
					lot[i].start()
					user_assigned = True
					#A thread has been assigned to the new user, move on to another user
				
					print("Started new user: %s"%user)
					print("Finished %d users"%users_finished)

					#Update every 30 users
					if users_finished % 30 == 0:
						update_api.post('https://api-parler-scrape.azurewebsites.net/update_desktop', data={'users_finished':users_finished})
				
					#delay = randint(delay_lb, delay_ub)
					users_finished += 1
				
					#time.sleep(delay)
				
					break 

#Waiting for all final 10 threads to finish
for thread in lot:
	thread.join()
