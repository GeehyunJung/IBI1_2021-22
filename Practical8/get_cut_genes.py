import os
import re
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical8/')
afile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
newfile=open('cut_genes','w')
for line in afile:
    if 'GAATTC' in line:
        newfile.write(line)
newfile.close()
acn=open('cut_genes.fa')
for line in acn:
    print(line[:-1])