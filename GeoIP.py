import urllib.request, re, json

def geoip():
	file = input('Enter text file with IPs to lookup:')
	inputfile = open(file,'r')

	iplist = []
	for line in inputfile.readlines():
		for imatch in re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line):
			iplist.append(imatch.group(1))

	output = open('geoip_output.csv','w',encoding='utf-8',errors='ignore')
	print('IP,Country_Code,Country,State,State_Code,City,ZIP,Time_Zone,Lat,Long,Metro_Code',file=output)
	output2 = open('geoip_output.txt','w',encoding='utf-8',errors='ignore')
	print('IP\tCountry_Code\tCountry\tState\tState_Code\tCity\tZIP\tTime_Zone\tLat\tLong\tMetro_Code',file=output2)
	
	count = 0
	for ip in iplist:
		url = 'https://freegeoip.net/json/' + ip
		geourl = urllib.request.urlopen(url).read().decode('utf-8',errors='strict')
		geo = json.loads(geourl)
		geo = (ip + '\t' + geo['country_code'] + '\t' + geo['country_name'] + '\t' + \
                       geo['region_name'] + '\t' + geo['region_code'] + '\t' + geo['city'] + '\t' \
                       + geo['zip_code'] + '\t' + geo['time_zone'] + '\t' + str(geo['latitude']) + '\t' \
                       + str(geo['longitude']) + '\t' + str(geo['metro_code']))
		print(geo)
		print(geo,file=output2)
		geo = geo.replace('\t',',')
		print(geo,file=output)
		count += 1
	print('Located ' + str(count) + ' IP addresses')

geoip()

