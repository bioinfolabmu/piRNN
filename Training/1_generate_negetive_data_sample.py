#2017-01-03
#Kai Wang
#usage: python 1_generate_negetive_data_sample.py piRNA.fa microRNA.fa tRNA.fa >nege.fa

import sys
from sys import argv
import random

nege_seq = []
#1. generate random sequences from 1st Markov chain
#############################
def get_first(A,C,G,T):
	"this function is to get the first nt for the random sequence"
	total = A + C + G + T
	rn = random.uniform(0,total)
	lt1 = A
	lt2 = lt1 + C
	lt3 = lt2 + G
	lt4 = lt3 + T

	if rn < lt1:
		ot = "A"
	elif rn < lt2 and rm >= lt1:
		ot = "C"
	elif rn < lt3 and rm >= lt2:
		ot = "G"	
	elif rn < lt4 and rm >= lt3:
		ot = "T"

def getlength(min_cd,max_cd):
	"get the sequence length"
	leng = random.randrange(min_cd, max_cd+1, 1)
	return leng

def getnext(nt,mat):
	"this fucntion is used to get the next nt based on the probability matirx"
	# if the first nt is A, the get the four numbers of A from the matrix to get the next nt
	# same for other cases
	if nt == 'A':
		lt1 = mat[0]
		lt2 = lt1 + mat[1]
		lt3 = lt2 + mat[2]
		lt4 = lt3 + mat[3]
		rn = random.uniform(0,lt4)
		if rn < lt1:
			next_nt = 'A'
		elif rn < lt2 and rn >= lt1:
			next_nt = 'G'
		elif rn < lt3 and rn >= lt2:
			next_nt = 'C'
		elif rn < lt4 and rn >= lt3:
			next_nt = 'T'
	elif nt == 'G':
		lt1 = mat[4]
		lt2 = lt1 + mat[5]
		lt3 = lt2 + mat[6]
		lt4 = lt3 + mat[7]
		rn = random.uniform(0,lt4)
		if rn < lt1:
			next_nt = 'A'
		elif rn < lt2 and rn >= lt1:
			next_nt = 'G'
		elif rn < lt3 and rn >= lt2:
			next_nt = 'C'
		elif rn < lt4 and rn >= lt3:
			next_nt = 'T'
	elif nt == 'C':
		lt1 = mat[8]
		lt2 = lt1 + mat[9]
		lt3 = lt2 + mat[10]
		lt4 = lt3 + mat[11]
		rn = random.uniform(0,lt4)
		if rn < lt1:
			next_nt = 'A'
		elif rn < lt2 and rn >= lt1:
			next_nt = 'G'
		elif rn < lt3 and rn >= lt2:
			next_nt = 'C'
		elif rn < lt4 and rn >= lt3:
			next_nt = 'T'
	elif nt == 'T':
		lt1 = mat[12]
		lt2 = lt1 + mat[13]
		lt3 = lt2 + mat[14]
		lt4 = lt3 + mat[15]
		rn = random.uniform(0,lt4)
		if rn < lt1:
			next_nt = 'A'
		elif rn < lt2 and rn >= lt1:
			next_nt = 'G'
		elif rn < lt3 and rn >= lt2:
			next_nt = 'C'
		elif rn < lt4 and rn >= lt3:
			next_nt = 'T'
	return next_nt

def read_fasta(fp):
	"this function is used for read fasta file"
	name, seq = None, []
	for line in fp:
		line = line.rstrip()
		if line.startswith(">"):
			if name: yield (name, ''.join(seq))
			name, seq = line, []
		else:
			seq.append(line)
	if name: yield (name, ''.join(seq))
#############################
# this is used for get the matirx
# since we use the 1st markov chain
# in total 16 numbers will be calculated and put into the matrix
fp = open(argv[1],'r')

i = 0 # i is used for count sequence numbers, this step will procude 50% sequences for negetive sample

sub_lt = []
max_cd = ''
min_cd = ''

AA = 0
AG = 0
AC = 0
AT = 0
GA = 0
GT = 0
GC = 0
GG = 0
CC = 0
CT = 0
CA = 0
CG = 0
TA = 0
TG = 0
TC = 0
TT = 0
# use a moving window (2 nt) to go throught all the sequences
for line in fp.readlines():
	line = line.strip('\n')
	if line.startswith('>'):
		i = i + 1
	else:
		cd = len(line)
		if min_cd:
			if min_cd <= cd:
				min_cd = min_cd
			else:
				min_cd = cd
		else:
			min_cd = cd
		if max_cd:
			if max_cd >= cd:
				max_cd = max_cd
			else:
				max_cd = cd
		else:
			max_cd = cd
		for j in range(len(line)-1):
			substr = line[j:j+2]
			frist  = substr[0]
			second = substr[1]
			if frist ==  'A':
				if second == 'A':
					AA = AA + 1
				elif second == 'G':
					AG = AG + 1
				elif second == 'C':
					AC = AC + 1
				elif second == 'T':
					AT = AT + 1
			elif frist == 'G':
				if second == 'A':
					GA = GA + 1
				elif second == 'G':
					GG = GG + 1
				elif second == 'C':
					GC = GC + 1
				elif second == 'T':
					GT = GT + 1
			elif frist == 'C':
				if second == 'A':
					CA = CA + 1
				elif second == 'G':
					CG = CG + 1
				elif second == 'C':
					CC = CC + 1
				elif second == 'T':
					CT = CT + 1
			elif frist == 'T':
				if second == 'A':
					TA = TA + 1
				elif second == 'G':
					TG = TG + 1
				elif second == 'C':
					CT = CT + 1
				elif second == 'T':
					TT = TT + 1
sub_lt.append(AA)
sub_lt.append(AG)
sub_lt.append(AC)
sub_lt.append(AT)

sub_lt.append(GA)
sub_lt.append(GG)
sub_lt.append(GC)
sub_lt.append(GT)

sub_lt.append(CA)
sub_lt.append(CG)
sub_lt.append(CC)
sub_lt.append(CT)

sub_lt.append(TA)
sub_lt.append(TG)
sub_lt.append(TC)
sub_lt.append(TT) 

total_A = AA * 2 + AG + AC + AT + GA + CA + TA
total_G = GA + GG * 2 + GC + GT + AG + CG + TG
total_C = CA + CG + CC * 2 + CT + AC + GC + TC
total_T = TA + TG + TC + TT * 2 + AT + GT + CT

num = int(i / 2) # half of negetive sample are generated from here

# this loop is used for generate sequences
# once the sequence length meet the length requirement, then jump out of the while loop and put the sequence into negetive set
for index in range(num):
	leng = getlength(min_cd - 1, max_cd)
	seq = getfirst(toatl_A, total_G, total_C, total_T)
	while(1):
		next_nt = getnext(seq[-1],sub_lt)
		seq = seq + next_nt
		if len(seq) == leng:
			break
	nege_seq.append(seq)
	seq = ""	

fp.close()

##############################
#2. read the microRNA file
micro = open(argv[2],'r')
mi_num = 0
for ids,seqs in read_fasta(micro):
	mi_num = mi_num + 1
	nege_seq.append(seqs)
micro.close()
###############################
#3. get sequence from tRNA
remain = int(i - (i / 2 + mi_num))

temp = []
trna = open(argv[3],'r')

for ids, seqs in read_fasta(trna):
	temp.append(seqs)

for ins in range(remain):
	leng = getlength(min_cd-1, max_cd)
	seq_ins = int(random.uniform(0,len(temp)))
	seq = temp[seq_ins]
	if len(seq) <= leng:
		redo
	else:
		ran = int(random.uniform(0,len(seq)-leng))
		nege_seq.append(seq[ran:(ran + leng)])
trna.close()
###############################
random.shuffle(nege_seq) #shuffle the list

for i in range(len(nege_seq)):
	print'>nege_%d'%i
	print(nege_seq[i])