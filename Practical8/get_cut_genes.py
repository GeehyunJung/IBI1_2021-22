import os
import re
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical8/')
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
myfile=open('cut_genes.fa','w')
gene_number=0
gene=[]
current_gene=''
# '>' indicates a new line
for line in xfile:
    #delete \n between lines
    line=line.replace('\n','')
    if line.startswith('>'):
        gene_number+=1
        #if 'GAATTC' in line, write it in the cut_genes.fa
        if gene_number>1:
            if 'GAATTC' in current_gene:
                myfile.write(current_gene+'\n')
        #if line do not startswith '>' add the line to the current gene to make it in one line
        current_gene=''
        continue
    current_gene+=line
# add the last line because not include in the loop
if 'GAATTC' in current_gene:
    myfile.write(current_gene)
myfile.close()