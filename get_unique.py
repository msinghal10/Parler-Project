from os import listdir
import json

list_of_files = listdir('./data')

for i in range(len(list_of_files)):
	list_of_files[i] = './data/'+list_of_files[i]

usernames = []

total_files = len(list_of_files)
file_current = 0

for file in list_of_files:
	with open(file) as f:
		data = json.load(f)
		for entry in data:
			if entry['username'] in usernames:
				continue
			else:
				usernames.append(entry['username'])

	print('Files finished %d'%file_current)
	file_current += 1

with open('test.txt', 'w') as f:
	for line in usernames:
		f.write(line)
		f.write('\n')