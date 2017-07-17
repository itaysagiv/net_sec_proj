#receives a csv file contains pcap data
#delete every thing - and add headers

import csv as csv
import sys
'''
clean the csv from pld data and write the headers
'''
file_path = sys.argv[1]
fieldnames = ['total_length', 'pkt_number', 'time_from_last_packet',
			  'time_since_first_packet', 'decision']
with open(file_path, 'w') as f:
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	f.close
	exit(1)
