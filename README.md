# python_challenge
Python Challenge

Use Parse.py to locate all IP addresses listed in a text file and print IP addresses to IPs_parsed.txt.
Parse.py accepts the name of the text file to be parsed as input

GeoIP.py will perform a GeoIP query on IP addresses and print data to geoip_output.txt and geoip_output.csv.
As input, GeoIP.py accepts the name of the text file that includes IP addresses to be located

RDAP.py will perform a RDAP query on IP addresses and print data to rdap_output.txt and rdap_output.csv.
As input, RDAP.py accepts the name of the text file that includes IP addresses to be queried

IP_Query.py allows the user to filter GeoIP and RDAP query results by a number of options.
IP_Query.py accepts the outputs of GeoIP.py (geoip_output.txt) and RDAP.py (rdap_output.txt) as input.
IP_Query.py outputs the query results to the console as well as to query_output.txt.
