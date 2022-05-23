import os
from xml.dom.minidom import parse as xml_parse
import matplotlib.pyplot as plt
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical14/')
tree=xml_parse('go_obo.xml')
root = tree.documentElement
term_list=root.getElementsByTagName("term")
print('The total number of terms is',len(term_list))

a={}
for term in term_list:
    is_a_list=[]
    for i in term.getElementsByTagName('is_a'):
        is_a_list.append(i.childNodes[0].data)
    id_list= term.getElementsByTagName('id')[0].childNodes[0].data
    for is_a in is_a_list:
        if is_a in a:
            a[is_a].append(id_list)
        else:
            a[is_a]=[id_list]

def counter(list_):
    for i in list_:
        if i not in list0:
            list0.append(i)
            if i in a:
                counter(a[i])
    return len(list0)
totallist=[]

for term in term_list:
    childnodes=0
    list0=[]
    id_list=term.getElementsByTagName('id')[0].childNodes[0].data
    if id_list in a:
        childnodes=counter(a[id_list])
    totallist.append(childnodes)

translist=[]
for term in term_list:
    if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data:
        id_list=term.getElementsByTagName('id')[0].childNodes[0].data
        if id_list in a:
            childnodes=counter(a[id_list])
        translist.append(childnodes)
plt.boxplot(totallist,
labels=['GO'],
vert=False,#vertical or not
showmeans=True,#show the mean or not
meanline=True,#show the mean in line or not
notch = False)
plt.title("the distribution of childnodes across terms")
plt.ylabel('number of childnodes')
plt.show()
plt.boxplot(translist,
labels=['translation GO'],
vert=False,#vertical or not
showmeans=True,#show the mean or not
meanline=True,#show the mean in line or not
notch = False)
plt.title("the distribution of childnodes across translation terms")
plt.ylabel('number of childnodes')
plt.show()
avg1=sum(totallist)/len(totallist)
avg2=sum(translist)/len(translist)
if avg1>avg2:
    print("The translation terms have a smaller number of childnodes than the overall Gene Ontology on average.")
if avg1<avg2:
    print("The translation terms have a greater number of childnodes than the overall Gene Ontology on average.")
