import re

#provide path to .txt file containing ip addresses to be parsed
def parse(file):
        inputfile = open(file,'r')
        iplist = []
        for line in inputfile.readlines():
                for match in re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line):
                        iplist.append(match.group(1))
        return iplist

		


