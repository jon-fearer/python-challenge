import urllib.request, re, json

def rdap():
	file = input('Enter text file with IPs to lookup:')
	inputfile = open(file,'r')

	iplist = []
	for line in inputfile.readlines():
		for imatch in re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line):
			iplist.append(imatch.group(1))
			
	output = open('rdap_output.csv','w',encoding='utf-8',errors='ignore')
	print('IP,StartBlock,EndBlock,Name',file=output)
	output2 = open('rdap_output.txt','w',encoding='utf-8',errors='ignore')
	print('IP\tStartBlock\tEndBlock\tName',file=output2)

	count = 0
	for ip in iplist:
		url = 'http://rdap.arin.net/bootstrap/ip/' + ip
		try:
			with urllib.request.urlopen(url) as rdapquery:
				jsonrdap = json.loads(rdapquery.read().decode('utf-8'))
				if 'name' in jsonrdap.keys():
					iprdap = ip + ',' + jsonrdap['startAddress'] + ',' + jsonrdap['endAddress'] + ',' + jsonrdap['name']
				elif 'startAddress' in jsonrdap.keys():
					iprdap = ip + ',' + jsonrdap['startAddress'] + ',' + jsonrdap['endAddress']
				else:
					iprdap = ip
				print(iprdap)
				print(iprdap,file=output)
				iprdap = iprdap.replace(',','\t')
				print(iprdap,file=output2)
				count += 1
		except urllib.error.URLError as e:
			print(ip+' '+e.reason)
			continue
	
	print('Located ' + str(count) + ' IP addresses')

rdap()
