#!/bin/bash

TRAIN_PCAP="train_pcap.pcap"
TEST_PCAP="test_pcap.pcap"
VECTOR="1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"

clear

#creating new clean files
python clean_csv.py test_pcap.csv
python clean_csv.py data_sniff_from_pcap_wireshark.csv
python clean_csv.py results.csv

#train set
python wireshark_from_pcap $TRAIN_PCAP $VECTOR
#test set
python wireshark_test_from_pcap $TEST_PCAP

#predict
for ALGO in rf bost knn Etree lda Etrees k-means do
	echo $ALGO:
	python predict_vector.py data_sniff_from_pcap_wireshark.csv $ALGO test_pcap.csv
done

#TO DO
#call model_selection to determain what algorithms to call on predict_vector
#avg predict_vector results to decide on a prediction
