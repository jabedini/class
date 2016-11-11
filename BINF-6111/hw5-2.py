file = open('hw5.vcf' , 'r')
f = []
hw5 = []
nhw5 = []

# remove the line that start with '##'

for line in file:
    if '##' in line:
        i = 0
    else:
        hw5.append(line)

# turn the file in to string 

for line in hw5:
	strline = str(line)
	strline.rstrip()
	nhw5.append(strline.split('\t'))
	
# remove lines 5,6,7,8 put it in the loop
#combine line 0 and 1
#reorder the lines 
#remove line 1

for line in nhw5:
	if len(line)>1:
		del line[5:9]
		line[0]= 'chr' + line[0]+':'+line[1]
		line[1]=line[2]
		line[2]=line[0]
		line[0]=line[1]
		line.pop(1)

#rename 2nd line	

nhw5[0][1]= 'COORDINATE'

#remove the extra characters only leaving 0|0
#skipping the first line
#on the row i>=1 break the items from 4th line and on m >= 4  keeping positions 0,1,2 
#do the same thing for the next line and the next row

i=0 
for line in nhw5:
	if len(line)==1:
		break
	if i >= 1:
		m=0
		for stuff in line:
			if m >= 4:
				nhw5[i][m] = nhw5[i][m][0:3]
				m=m+1
			else:
				m=m+1
		i=i+1
	else:
		i=i+1

#output the file
# '\n' not to add the stuff after each line 


out = open('hw5.vcf.out', 'w')
for line in nhw5:
	i= 0
	for stuff in line:
		if i == len(line)-1:
			out.write(stuff + '\n')
		else:
			out.write(stuff+'\t')
		i=i+1


