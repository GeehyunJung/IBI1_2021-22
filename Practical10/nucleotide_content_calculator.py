# input the sequence by the user
print('Plesase input your DNA sequence here: ')
origin_sequence=input()
# define a function that can change the sequence into upper letters
def sequence(x):
    x=list(x.upper())
    #calculate the percentage of different necleotides
    A_percentage=x.count('A')/len(x)
    T_percentage=x.count('T')/len(x)
    C_percentage=x.count('C')/len(x)
    G_percentage=x.count('G')/len(x)
    print(''.join(x))
    print('The precentages of A,T,C,G are:',A_percentage,T_percentage,C_percentage,G_percentage)
    return x
# use the function to get the sequence
new_sequence=sequence(origin_sequence)
# example
b='GTCaCGtccaaattt'
sequence(b)