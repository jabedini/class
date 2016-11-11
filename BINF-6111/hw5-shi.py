#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# input file:hw5.vcf
# output file: hw5.vcf.out (sort the coordinates of snps numerically in ascending order)

# Note: for multi-dimensional dictionary, you can use defaultdict by delaring "from collections import defaultdict"
snpLocTbl={} # [chr][pos]
snpAlleleTbl={} # [ID][REF/ALT]

genotypeTbl={} # [ID] 

sampleLst = [] # list of samples

###read data###
try:
    vcf= open('hw5.vcf')
    for line in vcf.readlines():
        line=line.rstrip()
        genotypeLst = [] # list of genotypes in the samples, the same order as in sampleLst
        if line.startswith('##'): #skip comments
            continue
        elif line.startswith('#'): # get sample names from header
            parts= line.split('\t')
            sampleLst = parts[9:] 
        else:
            parts= line.split('\t')
            if len(parts)>9: # make sure the line has at least one genotype field, simultaneously remove empty lines
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
                genotypeTbl[ID] = genoLst
        vcf.close
except:
    print("Cannot open input files!\n")


### output results ###
try:
    out= open('hw5.vcf.out', 'w')
    out.write("ID\tCOORDINATE\tREF\tALT\t" + ("\t".join(sampleLst))+ "\n")
    for chr in sorted(list(snpLocTbl.keys()), key=int): # first sort numerically on chr
        for pos in sorted(list(snpLocTbl[chr]), key=int): # then sort numerically on position
            ID = snpLocTbl[chr][pos]
            ref = snpAlleleTbl[ID]['REF']
            alt = snpAlleleTbl[ID]['ALT']
            out.write(ID + "\t" + "chr" + chr + ":" + pos + "\t" + ref + "\t" + alt + ("\t".join(genotypeTbl[ID]))+ "\n")
            out.close
except:
    print("Cannot open output files!\n")
