import sys
import os
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical8/')
sequence=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
gene=[]
current_gene=''
gene_number=0
gene_name=[]
for line in sequence:
    line=line.replace('\n','')
    if line.startswith('>'):
        for i in range(len(line)):
            if line[i:i+5]=='gene:':
                pos=i+6
                name=''
                while line[pos]!=' ':
                    name+=line[pos]
                    pos+=1
                gene_name.append(name)
        gene_number+=1
        gene.append(current_gene)
        current_gene=''
        continue
    current_gene+=line
gene.append(current_gene)
print('Please input the file name here:')
filename=sys.stdin.readline()
newfile=open(filename+'.fa','w')
for i in range(gene_number):
    current_gene = gene[i]
    gene_length = len(current_gene)
    for p in range(gene_length):
        if current_gene[p:p + 6] == 'GAATTC':
            newfile.write(gene_name[i]+' '+str(gene_length)+'\n'+current_gene+'\n')
            break
newfile.close()