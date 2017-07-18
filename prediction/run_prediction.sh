#!/bin/bash

TRAIN_PCAP="train_pcap.cap"
TEST_PCAP="test_pcap.cap"
VECTOR="1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"
SRC_IP='192.168.10.101'
DST_IP='192.168.10.103'
TEST='test'
TRAIN='train'
ALGO='rf'
clear

#creating new clean files
python clean_csv.py train_pcap.csv
python clean_csv.py test_pcap.csv

#train set
echo '--train parsing data--'
python -W ignore wireshark_fom_pcap.py $TRAIN_PCAP $VECTOR $SRC_IP $DST_IP $TRAIN
echo '--test parsing data--'
python -W ignore wireshark_fom_pcap.py $TEST_PCAP $VECTOR $SRC_IP $DST_IP $TEST
#test set
#python wireshark_test_from_pcap.py $TEST_PCAP 

#predict
#for ALGO in rf bost knn Etree lda Etrees k-means do
	#echo $ALGO:

	python -W ignore predict_vector.py train_pcap.csv $ALGO test_pcap.csv $VECTOR
done

#TO DO
#call model_selection to determain what algorithms to call on predict_vector
#avg predict_vector results to decide on a prediction
