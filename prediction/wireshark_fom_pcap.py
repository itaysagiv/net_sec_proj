#! /usr/bin/env python

#TO DO
#change getting known vector form args
#change getting pcap file form args
#finish num_of_vars - to do avg
#make this code do both train and test
	#add argv parameter - train or test
	#add if statment in main to devide the two cases
	#accordingly, chane the try block in costum_action

import pyshark
import csv
import sys
import re
'''
   first parmeter -file_path to pcap, 
	 second parameter-vector(currently unused)
		this code take pcap and parse it to csv(with known vector as decision column
		1-video, 0- photo
		important before each run you have to run clean.csv that cleans the csv and 
		write headers to it
'''

first_frame = 1
first_pkt_time=0.000000000000

file_path='data_sniff_from_pcap_wireshark.csv'
vector = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def num_of_vars(i):
	global num_of_vars
	num_of_vars[i]=num_of_vars[i]+1


def timing(time,time_from_last_packet):
	global counter,num_of_vars,vector
	index=int(time/5)
	#num_of_vars(index)
	#print int(time/5)
	return vector[index]

def custom_action(pkt):
	try:
		global first_frame,first_pkt_time,file_path
		#print pkt.frame_info
		transport_layer = pkt.transport_layer
		src_addr = pkt.ip.src
		dst_addr = pkt.ip.dst
		src_port = pkt[pkt.transport_layer].srcport
		dst_port = pkt[pkt.transport_layer].dstport
		sniff_timestamp = pkt.sniff_timestamp
		sniff_time = pkt.sniff_time
		total_length = pkt.length
		pkt_number = pkt.frame_info.number
		parts = re.split('\s|(?<!\d)[,.]', str(pkt.frame_info))
		time_from_last_packet = (parts[13])  # time from last packet
		time_since_first_packet = (parts[57])  # time since first packet

		time=float(time_since_first_packet)
		time=time-first_pkt_time
		if first_frame == 1:
			first_frame = 0
			first_pkt_time = time

		decision=timing(time,time_from_last_packet)
		fieldnames = [ 'total_length', 'pkt_number','time_from_last_packet',
					  'time_since_first_packet','decision']
	except AttributeError as e:
		# ignore packets that aren't TCP/UDP or IPv4
		print e
		pass

	try:
		with open(file_path, 'a') as f:
			writer = csv.DictWriter(f, fieldnames=fieldnames)
			writer.writerow({'total_length':total_length,'pkt_number':pkt_number
								,'time_from_last_packet':time_from_last_packet,
							'time_since_first_packet':time,
							'decision':decision })
			f.close()

	except:
		print e
		pass

if __name__ == "__main__":

	pcap_path = sys.argv[1]
	vector = map(int, sys.argv[2].split(','))
	src_ip = sys.argv[3]
	dst_ip = sys.argv[4]
	filt='ip.src == '+src_ip+' and ip.dst == '+dst_ip
	trahslist = ['method', '<bound', 'Ether', 'show', 'of', '<Ether', 'options=[]', '""', 'None)', '(', 'NOP',
				  '|<Raw', '|>>>>>','Ether(',')/ARP(']
	cap= pyshark.FileCapture(pcap_path,display_filter=filt)
	cap.apply_on_packets(custom_action)

