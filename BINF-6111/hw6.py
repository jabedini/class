snpLocTbl={} # [chr][pos]
snpAlleleTbl={} # [ID][REF/ALT]
RAfdic={}
genotypeTbl={} # [ID] 

sampleLst = [] # list of samples

raf = []

def RAF(genoLst):
	n=len(genoLst)
	N = 0
	for item in genoLst:
		if item == '0|0':
			N +=2
		elif item == '0|1':
			N +=1
		else: 
			N +=0
	myRAF = N/n
	return myRAF
			

###read data###
try:
	vcf = open('hw5.vcf','r')
	for line in vcf.readlines():
		line=line.rstrip()
		genotypeLst = [] 
		if line.startswith('##'): 
			continue
		elif line.startswith('#'): 
			parts= line.split('\t')
			sampleLst = parts[9:] 
		else:
			parts= line.split('\t')
			if len(parts)>9:
				chr = parts[0]
				pos = parts[1]
				ID = parts[2]
				snpLocTbl[chr] = snpLocTbl.get(chr, {})
				snpLocTbl[chr][pos] = ID
				ref = parts[3]
				alt = parts[4]
				snpAlleleTbl[ID] = snpAlleleTbl.get(ID, {})
				snpAlleleTbl[ID]['REF'] = ref
				snpAlleleTbl[ID]['ALT'] = alt
				genoLst = []
				for genoStr in parts[9:]:
					cols = genoStr.split(':')
					genoLst.append(cols[0])
				raf = str(RAF(genoLst))
				snpAlleleTbl[ID]['RAF'] = raf
		vcf.close
except:
    print("Cannot open input files!\n")


### output results ###
try:
    out= open('hw6.vcf.out', 'w')
    out.write("ID\tREF\tALT\tRAF" + "\n")
    for chr in sorted(list(snpLocTbl.keys()), key=int): # first sort numerically on chr
        for pos in sorted(list(snpLocTbl[chr]), key=int): # then sort numerically on position
            ID = snpLocTbl[chr][pos]
            ref = snpAlleleTbl[ID]['REF']
            alt = snpAlleleTbl[ID]['ALT']
            raf = snpAlleleTbl[ID]['RAF']
            out.write(ID + "\t" +  ref + "\t" + alt + "\t" + raf + "\t" + "\n")
            out.close
except:
    print("Cannot open output files!\n")
