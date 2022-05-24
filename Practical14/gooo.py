import os
from xml.dom.minidom import parse as xml_parse
import matplotlib.pyplot as plt
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical14/')
tree=xml_parse('go_obo.xml')
root = tree.documentElement
# term_list is the list for all terms. the terms are got by 'getElementsByTagName'
term_list=root.getElementsByTagName("term")
print('The total number of terms is',len(term_list))
#  the total_dic contains lists, whose names are the terms and contain the childnodes
total_dic={}
# find the id in the 'is_a' tag, and this is the parent node
for term in term_list:
    node_list=[]
    for i in term.getElementsByTagName('is_a'):
        node_list.append(i.childNodes[0].data)
    id_list= term.getElementsByTagName('id')[0].childNodes[0].data
    # create total_lic[parent node] and add the childnode (term) into the list
    for x in node_list:
        if x in total_dic:
            total_dic[x].append(id_list)
        else:
            total_dic[x]=[id_list]
# for each parent node, the childnode should contain the childnode itself and the childnode of the childnode
# function 'add' can add the childnodes of the child into the list of parent node, and calculate the lengh of the list
def add(x):
    for i in x:
        if i not in number_list:
            number_list.append(i)
            if i in total_dic:
                add(total_dic[i])
    return len(number_list)
# use function add to calculate the number of childnodes for the total list
total_list=[]
for term in term_list:
    total_number=0
    id_list=term.getElementsByTagName('id')[0].childNodes[0].data
    childnodes=0
    number_list=[]
    if id_list in total_dic:
        childnodes=add(total_dic[id_list])
    total_list.append(childnodes)
    # calculate the total number of childnodes
    total_number+=childnodes
# use the function add again with the terms associated with translation
translation=[]
for term in term_list:
    translation_number=0
    if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data:
        id_list=term.getElementsByTagName('id')[0].childNodes[0].data
        if id_list in total_dic:
            childnodes=add(total_dic[id_list])
        translation.append(childnodes)
        #calculate the total number of childnodes
        translation_number+=childnodes
# draw the boxplot
plt.boxplot(total_list,
labels=['GO'],
vert=False,#vertical or not
showmeans=True,#show the mean or not
meanline=True,#show the mean in line or not
notch = False)
plt.title("the distribution of childnodes of total terms")
plt.ylabel('number of childnodes')
plt.show()
plt.boxplot(translation,
labels=['translation GO'],
vert=False,#vertical or not
showmeans=True,#show the mean or not
meanline=True,#show the mean in line or not
notch = False)
plt.title("the distribution of childnodes of terms associated with translation")
plt.ylabel('number of childnodes')
plt.show()
#calculate the average number of the total and tranlation terms and compare them with each other
total=total_number/len(total_list)
trans=translation_number/len(translation)
if total>trans:
    print("The translation terms have a smaller number of childnodes than the overall Gene Ontology on average.")
if total<trans:
    print("The translation terms have a greater number of childnodes than the overall Gene Ontology on average.")