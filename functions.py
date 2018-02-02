#functions
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization, Activation
from keras.optimizers import Adam
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import load_model
#read fasta
def read_fasta(fa):
	name, seq = None, []
	for line in fa:
		line = line.strip()
		if line.startswith(">"):
			if name: yield(name, ''.join(seq))
			name, seq = line, []
		else:
			seq.append(line)
	if name: yield (name, ''.join(seq))
#get the kmer
def get_kmer(seq):
	ntarr = ("A","G","C","T")

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
		item = seq.count(kmerre[n])
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
		if "N" not in i:
			inx = kmerre.index(i)
			rst[inx] += 1

	for n in range(len(rst)):
		rst[n] = rst[n]/total

	return rst
#prediction
def prediction(dat, sp):

	if sp == 1:
		model = load_model('Ele_piRNN.h5')
	elif sp == 2:
		model = load_model('Dro_piRNN.h5')
	elif sp == 3:
		model = load_model('Rat_piRNN.h5')
	elif sp == 4:
		model = load_model('Hum_piRNN.h5')

	Y = model.predict_classes(dat, verbose = 0)

	return(Y)
#output
def output(Y_pre, ids, dics):
	new_dict = {}
	for i in range(len(Y_pre)):
		if Y_pre[i] == 1:
			new_dict[ids[i]] = dics[ids[i]]
	return(new_dict)
