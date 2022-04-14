import os
import re
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical8/')
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
myfile=open('cut_genes.fa','w')
gene_number=0
gene=[]
current_gene=''
for line in xfile:
    line=line.replace('\n','')
    if line.startswith('>'):
        gene_number+=1
        if gene_number>1:
            if 'GAATTC' in current_gene:
                myfile.write(current_gene+'\n')
        current_gene=''
        continue
    current_gene+=line
if 'GAATTC' in current_gene:
    myfile.write(current_gene)
myfile.close()
