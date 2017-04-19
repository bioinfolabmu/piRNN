#!/usr/bin/python
#parameter check
import argparse
parser = argparse.ArgumentParser(description='Instruction of piRNN(more details in README.txt):')
parser.add_argument('-i','--input_file', help='Input file in fasta format',required=True)
parser.add_argument('-s','--species',help='1: C.elegans  2: Drosophila  3: Rat  4: Human ', required=True)
parser.add_argument('-o','--output_file',help='Output file in fasta format', required=True)
args = parser.parse_args()

#import packages
import sys 
import numpy as np
import pandas
from functions import read_fasta
from functions import get_kmer
from functions import prediction
from functions import output

#read the file
file = open(args.input_file, 'r')
print("Loading Data ...")
seq_mat = []
seq_dic = {}
seq_id  = []
for ID, seq in read_fasta(file):
	mat = []
	mat = get_kmer(seq)
	seq_mat.append(mat)
	seq_dic[ID] = seq
	seq_id.append(ID)

#prepare data for prediction
dataframe = pandas.DataFrame(seq_mat)
dataset = dataframe.values
X = dataset[:,0:341].astype(float)

#prediction
print("Loading Model and predicting ...")
sp = int(args.species)
out = prediction(X, sp)

#get piRNA sequences
piRNA = output(out, seq_id, seq_dic)#piRNA is a dict to store the piRNA sequences from the prediction result

#get the output file
out = open(args.output_file,'w+')
print("piRNA are saving in %s ..." % args.output_file)
for k,v in piRNA.items():
	out.write(k)
	out.write("\n")
	out.write(v)
	out.write("\n")
