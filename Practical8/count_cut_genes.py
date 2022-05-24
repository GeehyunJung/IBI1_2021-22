import sys
import os
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical8/')
sequence=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
gene=[]
current_gene=''
gene_number=0
gene_name=[]
# make one DNA sequence in one line
for line in sequence:
    line=line.replace('\n','')
    if line.startswith('>'):
        for i in range(len(line)):
            # store all the names of the gene in gene_name
            if line[i:i+5]=='gene:':
                pos=i+5
                name=''
                while line[pos]!=' ':
                    name+=line[pos]
                    pos+=1
                gene_name.append(name)
        gene_number+=1
        # add all the genes( one gene in one line) in gene
        gene.append(current_gene)
        current_gene=''
        continue
    current_gene+=line
gene.append(current_gene)
#let the user input the filename and make sure it is FASTA format
print('Please input the file name here:')
filename=sys.stdin.readline()
newfile=open(filename+'.fa','w')
# choose the genes which have GAATTC and write it in the new file
for i in range(gene_number):
    current_gene = gene[i]
    gene_length = len(current_gene)
    for p in range(gene_length):
        if current_gene[p:p + 6] == 'GAATTC':
            fragments=current_gene.find('GAATTC')
            newfile.write('>'+gene_name[i]+'\n'+'The number of sequence that can be cut by EcoRI:'+str(fragments+1)+'\n'+current_gene+'\n')
            break
newfile.close()
# the example.fa is also uploaded in the folder