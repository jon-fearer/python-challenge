import re

def parse(file):
        inputfile = open(file,'r')
        iplist = []
        for line in inputfile.readlines():
                for match in re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line):
                        iplist.append(match.group(1))
        return iplist

		


