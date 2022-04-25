fname=input('input the file name:')
with open(fname,'w')as zfile:
    #copy codes from get_cut_genes.py:
    import re
    #read the file:
    with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')as xfile:
    #DEBUG:count=0
        orgg=''
        inf=''
        name=''
        for g in xfile.readlines():
            if re.match(r'^>',g):#only if the line starts with'>', aiming at faster speeds.
                  if re.search(r'GAATTC',orgg):
                      #DEBUG:count+=1
                      #DEBUG:print(orgg)
                      #extract information needed:
                      name=re.findall(r'gene:(.+?)\s',inf)[0]#rrefer to URL: https://www.cnpython.com/qa/42873
                      leng=len(orgg)
                  
                      #print out matching information:
                      
                      zfile.write('>')
                      zfile.write(name)
                      zfile.write('      ')
                      zfile.write(str(leng)+'\n')
                      zfile.write(orgg+'\n')
                  
                  inf=g
                  #DEBUG:print(orgg) 
                  orgg=''
            else:
                  #avoid sequences spanning two lines:              
                  g=g.rstrip()
                  #keep inputting dna sequence:
                  orgg+=g
         
        #DEBUG:print(count)
    
    
