import re

geotable = open('geoip_output.txt','r',encoding='utf-8',errors='ignore')
rdaptable = open('rdap_output.txt','r',encoding='utf-8',errors='ignore')

d1 = {}
d2 = {}

def builddict(table,dict):
	for line in table.readlines():
		for match in re.finditer(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\t(.+)$',line):
			dict[match.group(1)] = match.group(2)

builddict(table=geotable,dict=d1)
builddict(table=rdaptable,dict=d2)

def query(var,dict,col):
	print('IP\tCountry_Code\tCountry\tState\tState_Code\tCity\tZIP\tTime Zone\tLat\tLong\tMetro Code\tStartBlock\tEndBlock\tName')
	print('IP\tCountry_Code\tCountry\tState\tState_Code\tCity\tZIP\tTime Zone\tLat\tLong\tMetro Code\tStartBlock\tEndBlock\tName',file=output)
	for ip in dict.keys():
		if var == dict[ip].split("\t")[col]:
			try:
				print(ip+'\t'+d1[ip]+'\t'+d2[ip])
				print(ip+'\t'+d1[ip]+'\t'+d2[ip],file=output)
			except:
				print(ip+'\t'+dict[ip])
		elif var == ip:
			try:
				print(ip+'\t'+d1[ip]+'\t'+d2[ip])
				print(ip+'\t'+d1[ip]+'\t'+d2[ip],file=output)
			except:
				print(ip+'\t'+dict[ip])

output = open('query_output.txt','w')

def lookup():
	search = input('Searching by IP, Country Code, State Code, City, ZIP or Name?')
	if search == 'IP':
		ip = input('Enter IP address:')
		query(var=ip,dict=d1,col=0)
	elif search == 'Country Code':
		cc = input('Enter Country Code:')
		query(var=cc,dict=d1,col=0)
	elif search == 'State Code':
		st = input('Enter State Code:')
		query(var=st,dict=d1,col=3)
	elif search == 'City':
		city = input('Enter City:')
		query(var=city,dict=d1,col=4)
	elif search == 'ZIP':
		zip = input('Enter ZIP:')
		query(var=zip,dict=d1,col=5)
	elif search == 'Name':
		name = input('Enter Name:')
		query(var=name,dict=d2,col=-1)
	else:
		print('Unclear input. Try again')
		
lookup()
	
		
