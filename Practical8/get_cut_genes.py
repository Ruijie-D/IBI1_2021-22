import re
#read the file:
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')as xfile:
    #DEBUG:count=0
    orgg=''
    inf=''
    name=''
    fout=open('cut_genes.fa','w')
    for g in xfile.readlines():
        if re.match(r'^>',g):#only if the line starts with'>', aiming at faster speeds.
              if re.search(r'GAATTC',orgg):
                  #DEBUG:count+=1
                  #DEBUG:print(orgg)
                  #extract information needed:
                  name=re.findall(r'gene:(.+?)\s',inf)[0]#rrefer to URL: https://www.cnpython.com/qa/42873
                  leng=len(orgg)
                  
                  #print out matching information:
                  
                  fout.write('>')
                  fout.write(name)
                  fout.write('      ')
                  fout.write(str(leng)+'\n')
                  fout.write(orgg+'\n')
                  
              inf=g
              #DEBUG:print(orgg) 
              orgg=''
        else:
              #avoid sequences spanning two lines:              
              g=g.rstrip()
              #keep inputting dna sequence:
              orgg+=g
    fout.close()     
#DEBUG:print(count)
