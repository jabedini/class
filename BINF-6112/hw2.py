


class Genes():
    info={}
    source = []           
    def get_dic (self):
        infile = "hw2_hla.gb.txt"
        parsed = []
        with open(infile,'r') as file:
            for line in file:
                string = line.strip('\n')
                parsed.append(string)
                if string.startswith('  '+'ORGANISM'):
                        print (string)
                if string.startswith('VERSION'):
                        GI=string.split("GI:")[1]
                        print ("GI:" + GI)
                if string.startswith('ACCESSION'):
                        print (string)
        


print("Jaleh Abedini")
print("jabedini@uncc.edu")


ghla = Genes()
ghla.get_dic()
