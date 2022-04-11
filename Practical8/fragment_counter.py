import re
seq='ATGCAATCGACTACGATCAATCGAGGGCC'
frg=re.findall(r'GAATTC',seq)
numf=0
if len(frg)>0:
  numf=len(frg)+1
print(numf)
