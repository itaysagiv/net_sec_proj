#! /usr/bin/env python
import pyshark
import csv
import sys
import re
'''
   first parmeter -file_path to pcap, 
		this code take pcap and parse it to test csv
		important before each run you have to run clean.csv that cleans the csv and 
		write headers to it
		'''
first_frame = 1
first_pkt_time=0.000000000000


def video_time(time):
	vector = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
	if 0.0 <= time < 5.0:
		return vector[0]
	elif 5.0 <= time < 10.0:
		return vector[1]
	elif 10.0 <= time < 15.0:
		return vector[2]
	elif 15.0 <= time < 20.0:
		return vector[3]
	elif 20.0 <= time < 25.0:
		return  vector[4]
	elif 25.0 <= time < 30.0:
		return  vector[5]
	elif 30.0 <= time < 35.0:
		return vector[6]
	elif 35.0 <= time < 40.0:
		return vector[7]
	elif 40.0 <= time < 45.0:
		return vector[8]
	elif 45.0 <= time < 50.0:
		return vector[9]
	elif 50.0 <= time < 55.0:
		return vector[10]
	elif 55.0 <= time < 60.0:
		return vector[11]
	elif 60.0 <= time < 65.0:
		return vector[12]
	elif 65.0 <= time < 70.0:
		return vector[13]
	elif 70.0 <= time < 75.0:
		return vector[14]


def each_5_sec_class(time):
	if  0.0 >= time < 5.0:
		return 1
	if 5.0 >= time < 10.0:
		return 2
	if 10.0 >= time < 15.0:
		return 3
	if 15.0 >= time < 20.0:
		return 4
	if 20.0 >= time < 25.0:
		return 5
	if 30.0 >= time < 35.0:
		return 6
	if 40.0 >= time < 45.0:
		return 7
	if 50.0 >= time < 55.0:
		return 8
	if 55.0 >= time < 60.0:
		return 9
	if 60.0 >= time < 65.0:
		return 10
	if 70.0 >= time < 75.0:
		return 11
	if 75.0 >= time < 80.0:
		return 12
	if 80.0 >= time < 85.0:
		return 13
	if 85.0 >= time < 90.0:
		return 14
	if 90.0 >= time < 95.0:
		return 15
	return 1


def custom_action(pkt):
		try:
			#print pkt.frame_info
			#udp_Length = pkt['UDP'].Length
			transport_layer = pkt.transport_layer
			src_addr = pkt.ip.src
			dst_addr = pkt.ip.dst
			src_port = pkt[pkt.transport_layer].srcport
			dst_port = pkt[pkt.transport_layer].dstport
			sniff_timestamp = pkt.sniff_timestamp
			sniff_time = pkt.sniff_time
			total_length = pkt.length
			pkt_number = pkt.frame_info.number
			# print pkt.frame_info
			parts = re.split('\s|(?<!\d)[,.]', str(pkt.frame_info))
			time_from_last_packet = (parts[13])  # time from last packet
			time_since_first_packet = (parts[57])  # time since first packet
			global first_frame
			global first_pkt_time
			if first_frame==1:
				first_pkt_time=float(time_since_first_packet)
				first_frame=0
			time=float(time_since_first_packet)
			time=time-first_pkt_time
			#print time
			decision=video_time(time)
			#print decision
			#if video_time(time):
			#	decision=1 #1 means video is on
			#else:
			#	decision=0 #0 means photo is on

			fieldnames = [ 'total_length', 'pkt_number','time_from_last_packet',
						  'time_since_first_packet','decision']
			#print '%s  %s:%s --> %s:%s' % (transport_layer, src_addr, src_port, dst_addr, dst_port)
		except AttributeError as e:
			# ignore packets that aren't TCP/UDP or IPv4
			pass

		try:
			with open('test_pcap.csv', 'a') as f:
				writer = csv.DictWriter(f, fieldnames=fieldnames)
				writer.writerow({'total_length':total_length,'pkt_number':pkt_number
									,'time_from_last_packet':time_from_last_packet,
								'time_since_first_packet':time,
								 })
				f.close()

		except:
			pass

if __name__ == "__main__":
	params=len(sys.argv)
	if params>1:
		file_path = sys.argv[1]
	trahslist = ['method', '<bound', 'Ether', 'show', 'of', '<Ether', 'options=[]', '""', 'None)', '(', 'NOP',
				  '|<Raw', '|>>>>>','Ether(',')/ARP(']
	cap= pyshark.FileCapture(file_path,display_filter='ip.src == 192.168.10.101 and ip.dst == 192.168.10.103 and'
													  ' udp.port==5555')

	#display_filter='ip.src == 192.168.1.20and ip.dst == 192.168.1.12'
	cap.apply_on_packets(custom_action)
	#file = 'wireshark_cap.csv'
