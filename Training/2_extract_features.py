#2017-01-03
#Kai Wang
#usage: python 2_extract_features.py piRNA.fa nege.fa 
# this code is same to the functions.py
import sys
from sys import argv
import random

######################################
def countoverlap(seq,kmer):
	return len([1 for i in range(len(seq)) if seq.startswith(kmer,i)])
######################################
def read_fasta(fa):
	name,seq = None, []
	for line in fa:
		line = line.strip()
		if line.startswith(">"):
			if name: yield (name, ''.join(seq))
			name,seq = line,[]
		else:
			seq.append(line)
	if name: yield (name, ''.join(seq))	
######################################
def get_kmer(seq):
	ntarr = ("A","C","G","T")

	kmerArray = []
	kmerre = []
	rst = []
	fst = 0
	total = 0.0
	pp = 0.0
	item = 0.0

	for n in range(4):
		kmerArray.append(ntarr[n])

	for n in range(4):
		str1 = ntarr[n]
		for m in range(4):
			str2 = str1 + ntarr[m]
			kmerArray.append(str2)
#############################################
	for n in range(4):
		str1 = ntarr[n]
		for m in range(4):
			str2 = str1 + ntarr[m]
			for x in range(4):
				str3 = str2 + ntarr[x]
				kmerArray.append(str3)
#############################################
#change this part for 3mer or 4mer
	for n in range(4):
		str1 = ntarr[n]
		for m in range(4):
			str2 = str1 + ntarr[m]
			for x in range(4):
				str3 = str2 + ntarr[x]
				for y in range(4):
					str4 = str3 + ntarr[y]
					kmerArray.append(str4)
############################################
	for i in ntarr:
		kmerre.append(i)
		for m in kmerArray:
			st = i + m
			kmerre.append(st)
############################################
	for n in range(len(kmerre)):
		item = countoverlap(seq,kmerre[n])
		total = total + item
		rst.append(item)

	sub_seq = []
	if seq.startswith("T"):
		sub_seq.append(seq[0:1])
		sub_seq.append(seq[0:2])
		sub_seq.append(seq[0:3])
		sub_seq.append(seq[0:4])
		sub_seq.append(seq[0:5])

	if seq[9:10] == "A":
		sub_seq.append(seq[9:10])
		sub_seq.append(seq[8:10])
		sub_seq.append(seq[7:10])
		sub_seq.append(seq[6:10])
		sub_seq.append(seq[5:10])
		sub_seq.append(seq[9:11])
		sub_seq.append(seq[9:12])
		sub_seq.append(seq[9:13])
		sub_seq.append(seq[9:14])

	for i in sub_seq:
		inx = kmerre.index(i)
		rst[inx] += 1

	for n in range(len(rst)):
		rst[n] = rst[n]/total

	return rst
########################################
po_file = open(argv[1],'r')

posi_set = []

for ID,seq in read_fasta(po_file):
	po_mat = []
	po_mat = get_kmer(seq)
	po_mat.append(1)
	posi_set.append(po_mat)

random.shuffle(posi_set)

posi_train = int(round(len(posi_set)*0.7))
posi_test  = int(round(len(posi_set)*0.2))
posi_valid = len(posi_set) - posi_train - posi_test


posi_train_set = posi_set[0:posi_train] 
posi_test_set  = posi_set[posi_train:posi_train+posi_test]
posi_valid_set = posi_set[posi_train+posi_test:len(posi_set)]
########################################
########################################
ne_file = open(argv[2],'r')

nega_set = []

for ID,seq in read_fasta(ne_file):
	ne_mat = []
	ne_mat = get_kmer(seq)
	ne_mat.append(0)
	nega_set.append(ne_mat)

random.shuffle(nega_set)

nega_train = int(round(len(nega_set)*0.7))
nega_test  = int(round(len(nega_set)*0.2))
nega_valid = len(nega_set) - nega_train - nega_test


nega_train_set = nega_set[0:nega_train] 
nega_test_set  = nega_set[nega_train:nega_train+nega_test]
nega_valid_set = nega_set[nega_train+nega_test:len(nega_set)]
########################################

train_set = posi_train_set + nega_train_set
test_set  = posi_test_set  + nega_test_set
valid_set = posi_valid_set + nega_valid_set

########################################

train = open("train.csv","w")

for n in train_set:
	train.write(",".join(map(str,n)))
	train.write("\n")

########################################

test = open("test.csv","w")

for n in test_set:
	test.write(",".join(map(str,n)))
	test.write("\n")

#########################################

valid = open("valid.csv","w")

for n in valid_set:
	valid.write(",".join(map(str,n)))
	valid.write("\n")