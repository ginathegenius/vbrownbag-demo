import csv, os, slack # import statements

# read csv with ip addresses 
with open('test.csv') as csvfile: 
	reader = csv.reader(csvfile,delimiter=',')
	# convert it to a list
	new_list = list(reader)
	# remove the first element in the list
	new_list.pop(0)
	output = ''
	# loop through csv list 
	for row in new_list:
		ip_addr = row[0]
		# ping each server 
		resp = os.system("ping -c 2 " + ip_addr)
		if resp == 0:
			output += ip_addr + ', is up!\n'
		else:
			output += ip_addr + ', is down!\n'

# open csv for writing
with open('output.csv','w', newline='') as fd:
	fd.write(output)

# define parameters for slack 
url = "https://hooks.slack.com/services/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"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

#call slack function
slack.slack('output.csv',url,headers)