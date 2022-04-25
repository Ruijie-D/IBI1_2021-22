import re
#read the file:
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
#DEBUG:count=0
orgg=''
inf=''
for g in xfile.readlines():
    if re.match(r'^>',g):#only if the line starts with'>', aiming at faster speeds.
          if re.search(r'GAATTC',orgg):
              #DEBUG:count+=1
              #DEBUG:print(orgg)
              ##extract information needed:
              name=re.findall(r'gene:(.+?)\s',inf)
              leng=len(orgg)
              #print out matching information:
              print('>',end='')#refer to URL:https://m.php.cn/article/471647.html
              print(name,end='')
              print('      ',end='')
              print(str(leng))
              print(orgg)
          inf=g
          #DEBUG:print(orgg) 
          orgg=''
    else:
          #avoid sequences spanning two lines:              
          g=g.rstrip()
          #keep inputting dna sequence:
          orgg+=g
#DEBUG:print(count)
