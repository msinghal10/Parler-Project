import requests, threading, time
from random import uniform
from csv import writer
import json	
import settings 
from subprocess import check_output

#Scraping stuff
op_file = 'data/'
delay_lb = 0.1
delay_ub = 1
update_api = requests.session()
key = ''
name = ''

#log_file
log_file_req = 'logs/requests.csv'

#Requests stuff
sesh = requests.session()
cookies = ''

#Threading stuff
num_of_threads = 35
lot = [None] * num_of_threads

users_finished = 0

#Check/Make settings for each instance
if settings.config_exists() == False:
	if input('No settings file found. Do you want to create a settings file?(y/n)') == 'y':
		settings.generate_config()
	else:
		print('Could not run program without settings file')
		quit()

#Read setings file and initialize new job with API
else:
	print("Settings file found!")
	config = settings.read_config()
	num_of_threads = config['threads']
	name = config['name']
	delay_lb = config['delay_lb']
	delay_ub = config['delay_ub']
	cookies = config['cookies']
	key = config['key']

def posting(pg):

	more_than_one = False

	dt = {'page': pg,
		'discover': True}

	headers = {'Host': 'parler.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://parler.com/user/OANN',
	'Content-Length': '286',
	'Origin': 'https://parler.com',
	'Connection': 'keep-alive',
	'Cookie': cookies,
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'no-cors',
	'Sec-Fetch-Site': 'same-origin',
	'Cache-Control': 'max-age=0, no-cache',
	'Pragma': 'no-cache'}

	while True:

		r = sesh.post('https://parler.com/pages/feed.php', data = dt, headers = headers)
		
		more_than_one = True

		page = r.json()
		with open(log_file_req, 'a+') as f:
			log_list = []
			#log_list.append(username)
			log_list.append(str(r.elapsed.total_seconds()))
			log_list.append(str(r.status_code))
			#log_list.append(str(pg))
			#log_list.append(str(iters))
			#log_list.append(str(delay))
			writer_obj = writer(f)
			writer_obj.writerow(log_list)

		#pg += 1
		file_name = str(time.time())
		gf = open(op_file+file_name+'_'+str(pg)+".json", "a+")
		json.dump(page,gf,indent=1)
		gf.close()

		break


update_api.get('https://api-parler-scrape.azurewebsites.net/start/'+key)

for i in range(1, 271):
	posting(i)
	delay = uniform(delay_lb, delay_ub)
	time.sleep(delay)

	users_finished += 1
	update_api.post('https://api-parler-scrape.azurewebsites.net/update/'+key, data={'users_finished':users_finished})
	print('Finished %d users'%users_finished)

