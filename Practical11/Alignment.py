import os
import pandas as pd
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical11/')
BLOSUM=pd.read_csv('BLOSUM.csv')

a=open('DLX5_human.fa','r')
b=open('DLX5_mouse.fa','r')
c=open('RandomSeq(1).fa','r')
def sequence(x):
    seq=[]
    for line in x:
        line=line.replace('\n','')
        if line.startswith('>'):
            continue
        seq.append(line)
    return seq
seqa=''.join(sequence(a))
seqb=''.join(sequence(b))
seqc=''.join(sequence(c))
class Percentage():
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def calculate(self):
        edit_distance=0
        for i in range(len(seqa)):
            if self.first[i]==self.second[i]:
                edit_distance+=1
        percentage=edit_distance/len(seqa)
        return percentage
    def score(self):
        score=0
        first_line = list(BLOSUM['First'])
        for i in range(len(seqa)):
            current_score=''
            for k in range(len(first_line)):
                if first_line[k] == self.second[i]:
                    number=k
            list1=list(BLOSUM[self.first[i]])
            current_score=list1[number]
            score+=current_score
        return score
A=Percentage(seqa,seqb)
B=Percentage(seqa,seqc)
C=Percentage(seqb,seqc)

print('The alignment score for DLX5_human and DLX5_mouse is',Percentage.score(A),'. And the percentage of identical amino acids is',Percentage.calculate(A))
print('The alignment score for DLX5_human and RandomSeq is',Percentage.score(B),'. And the percentage of identical amino acids is',Percentage.calculate(B))
print('The alignment score for DLX5_mouse and RandomSeq is',Percentage.score(C),'. And the percentage of identical amino acids is',Percentage.calculate(C))





