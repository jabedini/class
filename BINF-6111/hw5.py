##open the file and got the first line

file = open('hw5.vcf' , 'r')
f = []
hw5 = []
nhw5 = []
for line in file:
    if '##' in line:
        i = 0
    else:
        hw5.append(line)
        
for line in hw5:
	strline = str(line)
	strline.rstrip()
	nhw5.append(strline.split('\t'))
	
for line in nhw5:
		line.pop(5)
		line.pop(5)
		line.pop(5)
		line.pop(5)
		line[0]= 'chr' + line[0]+':'+line[1]
		line[1]=line[2]
		line[2]=line[0]
		line[0]=line[1]
		line.pop(1)

nhw5[0][1]= 'COORDINATE'
out = open('hw5.vcf.out', 'w')
for line in nhw5:
	i= 0
	for stuff in line:
		if i == len(line)-1:
			out.write(stuff)
		else:
			out.write(stuff+'\t')
		i=i+1
