from pickle import EMPTY_LIST
from xml.dom.minidom import parse 
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
terms=collection.getElementsByTagName("term")

#initialize the term-childNode dictionary (direct parent-child nodes):
Tm_chdNd={}
ttlch=[]
#calculate the total number:
i=0
for term in terms:
    i+=1
#calculate each term's childnodes:
    sn=term.getElementsByTagName('id')[0].childNodes[0].data
    if term.getElementsByTagName('is_a'):
        fts=term.getElementsByTagName('is_a')
        
        for m in range(fts.length):
            ft=fts.item(m).childNodes[0].data
            
            if ft in Tm_chdNd.keys(): #need to use Python 3
                Tm_chdNd[ft].append(sn)
            else:
                ll=[sn]
                Tm_chdNd[ft]=ll
    else:
        ttlch.append(0)
print("There are "+str(i)+" terms.")#There are 47340 terms.
                
#print(len(Tm_chdNd)) There are 17574 valid parentNodes thus 29766 parentNodes without childNodes.
#calculate the total childnodes including indirect ones:
def progeny(sub_l,key_l):
    vld_l=[]
    for d in range(len(sub_l)):
        if sub_l[d] in key_l:
            vld_l.append(sub_l[d])
    return vld_l#the list of all childNodes in the list with childNodes
            
key_ll=[*Tm_chdNd]#key list of the dic

for n in range(len(Tm_chdNd)):
    
    sub_ll=Tm_chdNd[key_ll[n]]#corresponding childNodes of the specific parentNode
    orig_len=len(set(sub_ll))
    
    if len(progeny(sub_ll,key_ll))!=0:#justify if childNodes have childNodes
        pro_ll=progeny(sub_ll,key_ll)
        for o in range (len(pro_ll)):
            for p in range (len(Tm_chdNd[pro_ll[o]])):
                sub_ll.append(Tm_chdNd[pro_ll[o]][p])
        while orig_len!=len(set(sub_ll)):#demonstrating the sub_ll has changed
            orig_len=len(set(sub_ll))
            rpro_ll=progeny(sub_ll,key_ll)
            
            if len(set(rpro_ll))!=len(set(pro_ll)):#has third or more level of childNodes
                for q in range (len(Tm_chdNd[pro_ll[o]])):
                    sub_ll.append(Tm_chdNd[pro_ll[o]][q])
                pro_ll=rpro_ll
                
    cnt=len(set(sub_ll))
    #print(cnt)
    ttlch.append(cnt)
#print(ttlch)


#find GO associated with "translation" and store them in a list:
ass_key=[]#store the GO associated with the trnaslation description
for term in terms:
    sn2=term.getElementsByTagName('id')[0].childNodes[0].data
    if term.getElementsByTagName('defstr'):
        dscbtxt=term.getElementsByTagName('defstr')[0].childNodes[0].data
        if dscbtxt.find('translation')>0:
            ass_key.append(sn2)
#extract the GO from the Tm_chdNd dictionary and store the childNodes number in a list:
chdNd_nb=[]
for r in range(len(ass_key)):
    if ass_key[r] in Tm_chdNd.keys():
        vl=Tm_chdNd[ass_key[r]]
        vl_nb=len(set(vl))
        chdNd_nb.append(vl_nb)
    else:
        chdNd_nb.append(0)


#BEGIN TO DRAW the two CHARTS!
import matplotlib.pyplot as plt
import numpy as np
#draw the first chart: 
plt.boxplot(
    ttlch,
    sym='o',
    whis=1.5,
    patch_artist=True, 
    meanline=True, 
    showbox=True, 
    showcaps=True, 
    showfliers=True,
    notch=False
    )
plt.title('the distribution of child nodes across all the terms')
plt.xlabel('total')
plt.ylabel('number')
plt.grid(linestyle="--",alpha=0.7)
plt.show()

#draw the second chart: 
plt.boxplot(
    chdNd_nb,
    sym='o',
    whis=1.5,
    )
plt.title("the distribution of child nodes across terms	associated with 'translation'")
plt.xlabel('translation')
plt.ylabel('number')
plt.grid(linestyle="--",alpha=0.7)
plt.show()

#compare the average value:
import numpy as np
if np.mean(ttlch)<np.mean(chdNd_nb):
	print("the translation terms contain a smaller number of child nodes than the overall Gene Ontology on average.")
elif np.mean(ttlch)>np.mean(chdNd_nb):
	print("the translation terms contain a greater number of child nodes than the overall Gene Ontology on average.")
else:
	print ("They contain an equal number of average child nodes on average.")
#comment of the result:
#the 'translation’ terms contain, a	greater number of child nodes than the overall Gene Ontology on average.	
#It take 8-9 min to run the codes.


  


