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
	for n in range(4):
		str1 = ntarr[n]
		for m in range(4):
			str2 = str1 + ntarr[m]
			for x in range(4):
				str3 = str2 + ntarr[x]
				kmerArray.append(str3)
	for n in range(4):
		str1 = ntarr[n]
		for m in range(4):
			str2 = str1 + ntarr[m]
			for x in range(4):
				str3 = str2 + ntarr[x]
				for y in range(4):
					str4 = str3 + ntarr[y]
					kmerArray.append(str4)
	for n in range(len(kmerArray)):
		item = seq.count(kmerArray[n])
		total = total + item
		rst.append(item)

	if seq.startswith("T"):
		fst = 1
	else:
		fst = 0
	for n in range(len(rst)):
		rst[n] = rst[n]/total


	rst.insert(0,fst)
	
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
