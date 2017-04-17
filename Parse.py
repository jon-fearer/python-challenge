import re

def main():
	file = input('Enter text file to be parsed:')
	inputfile = open(file,'r')
	output = open('IPs_parsed.txt','w')

	for line in inputfile.readlines():
		for match in re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line):
			print(match.group(1),file=output)

if __name__ == "__main__":
	main()
		


