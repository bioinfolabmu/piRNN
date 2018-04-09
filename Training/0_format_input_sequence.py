#2017-01-03
#Kai Wang
#usage: python 0_format_input_sequence.py input.fa >output.fa

from sets import Set
from sys import argv

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

f = open(argv[1],'r')

for Id,seq in read_fasta(f):
	seq_allow = Set("ACGT")
	if Set(seq).issubset(seq_allow):
		print(Id)
		print(seq)