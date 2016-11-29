from hw7_module import gc


with open('hw7.fa.txt','r') as infile, open('hw7.out', 'w') as outfile:
    Y = infile.read()
    mygc = gc(Y)
    outfile.write('Jaleh Abedini' + '\t' + str(mygc))
    
