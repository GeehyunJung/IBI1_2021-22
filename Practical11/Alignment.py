import os
import pandas as pd
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical11/')
BLOSUM=pd.read_csv('BLOSUM.csv')

a=open('DLX5_human.fa','r')
b=open('DLX5_mouse.fa','r')
c=open('RandomSeq(1).fa','r')
# define a function sequence() to read the protein sequence
def sequence(x):
    seq=[]
    for line in x:
        # delete '\n' at the end of each line
        line=line.replace('\n','')
        # '>' means a new protein sequence
        # if startwith '>' change to a new line, else add it to the line
        if line.startswith('>'):
            continue
        seq.append(line)
    return seq
# put the protein sequence into a list
seqa=''.join(sequence(a))
seqb=''.join(sequence(b))
seqc=''.join(sequence(c))
# generate a class to relate two sequence
class Percentage():
   # first and second are two sequence that will be compared
    def __init__(self,first,second):
        self.first=first
        self.second=second
    # generate a function
    # compare two lists (sequences) and calculate the edit_distance and the percentage
    def calculate(self):
        edit_distance=0
        for i in range(len(seqa)):
            if self.first[i]==self.second[i]:
                edit_distance+=1
        percentage=edit_distance/len(seqa)
        return percentage
    # generate another function to calculate the score
    def score(self):
        score=0
        # read the first line of the BLOSUM
        first_line = list(BLOSUM['First'])
        # for each protein in the first sequence
        # find the number of column and the number of line in the BLOSUM to get the score
        for i in range(len(seqa)):
            current_score=''
            for k in range(len(first_line)):
                # compare the first line with the second list
                # number means the number of column
                if first_line[k] == self.second[i]:
                    number=k
            # choose the line whose title is the same as first[i]
            # put them in the list
            list1=list(BLOSUM[self.first[i]])
            # the number of the column is the same as the number of element in the list
            # the exact score can be found
            current_score=list1[number]
            # add the current score together to get the final score
            score+=current_score
        return score
A=Percentage(seqa,seqb)
B=Percentage(seqa,seqc)
C=Percentage(seqb,seqc)

print('The alignment score for DLX5_human and DLX5_mouse is',Percentage.score(A),'. And the percentage of identical amino acids is',Percentage.calculate(A))
print('The alignment score for DLX5_human and RandomSeq is',Percentage.score(B),'. And the percentage of identical amino acids is',Percentage.calculate(B))
print('The alignment score for DLX5_mouse and RandomSeq is',Percentage.score(C),'. And the percentage of identical amino acids is',Percentage.calculate(C))





